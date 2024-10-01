<script setup lang="ts">
import { computed, onBeforeMount, onMounted, onUnmounted, ref, type ComputedRef, type Ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import {
  mdiShareVariantOutline,
  mdiCloseCircleOutline,
  mdiArrowLeft,
  mdiArrowRight,
  mdiAccountCircleOutline,
  mdiEmailOutline,
  mdiArrowDown,
} from '@mdi/js';

import { appRoutes } from '@/main';
import { useElectionStore } from '@/stores/electionStore';
import { useUserStore, type User } from '@/stores/userStore';
import {
  calculateRelativeAgreement,
  encodeResults,
} from '@/common/resultParser';

import type { DeprecatedElection } from '@/types/election';
import type { DeprecatedCandidateAnswer } from '@/types/candidate-answer';

import BackgroundComponent from '@/components/design-system/style/BackgroundComponent.vue';
import BottomBar from '@/components/design-system/navigation/BottomBar.vue';
import BottomBarWrapper from '@/components/design-system/layout/BottomBarWrapper.vue';
import CardComponent from '@/components/design-system/containers/CardComponent.vue';
import ButtonComponent from '@/components/design-system/input/ButtonComponent.vue';
import IconButton from '@/components/design-system/input/IconButton.vue';
import IconComponent from '@/components/design-system/icons/IconComponent.vue';
import NavigationBar from '@/components/design-system/navigation/NavigationBar.vue';
import SecondaryNavigationBar from '@/components/design-system/navigation/SecondaryNavigationBar.vue';
import StackComponent from '@/components/design-system/layout/StackComponent.vue';
import TextInputComponent from '@/components/design-system/input/TextInputComponent.vue';
import TitleText from '@/components/design-system/typography/TitleText.vue';

import EmbedWrapper from '@/components/utilities/embedding/EmbedWrapper.vue';
import ResponsiveWrapper from '@/components/utilities/ResponsiveWrapper.vue';
import StickyHeaderLayout from '@/components/layouts/StickyHeaderLayout.vue';

import ResultCategory from './ResultCategory.vue';
import ResultShareModal from './ResultShareModal.vue';
import { getDistrictCode } from '@/common/utils';
import BodyText from '../../components/design-system/typography/BodyText.vue';
import ErrorModal from '../../components/ErrorModal.vue';
import CheckboxComponent from '../../components/design-system/input/CheckboxComponent.vue';
import { inject } from 'vue';
import { EmbedKey } from '@/components/utilities/embedding/EmbedKey';

import { useI18n } from 'vue-i18n';
import { switchLanguage } from '@/i18n';

const { t, locale } = useI18n();

const currentEmbed = inject(EmbedKey);

const router = useRouter();
const route = useRoute();
const electionStore = useElectionStore();

const userStore = useUserStore();

const user = computed(() => userStore.user);

const election = electionStore.election as DeprecatedElection;
const electionName = election.name;
const districtCode = getDistrictCode(route.params.second as string);
const districtName = electionStore.districts.filter(
  (district) => district.district_code === districtCode,
)[0].name;
const showDistrictCode = electionStore.districts.filter(
  (district) => district.district_code === districtCode,
)[0].show_district_code;
const districtNameWithCode = showDistrictCode
  ? `${districtName} (${districtCode})`
  : districtName;

const breadcrumbs = ``;

const handlePreviousClick = () => {
  router.push({
    name: appRoutes.recap.name,
    params: { ...route.params },
    query: { ...route.query },
  });
};

const handleStartClick = () => {
  router.push({
    name: appRoutes.question.name,
    params: { ...route.params, nr: 1 },
    query: { ...route.query },
  });
};

const handleShowComparsionClick = () => {
  router.push({
    name: appRoutes.comparison.name,
    params: { ...route.params },
    query: { ...route.query },
  });
};

const goToForm = () => {
  const element = document.querySelector('a[name="jelentkezes"]');
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
};

const handleShareClick = () => {
  shareModal.value?.open();
};
onBeforeMount(async () => {
  if (userStore.user || userStore.user === null) {
    const res = await electionStore.saveResults({
      embedName: currentEmbed,
      user: userStore.user as User | null | undefined,
    });
    console.debug(res);
  } else {
    userStore.$subscribe(async (mutation, state) => {
      const res = await electionStore.saveResults({
        embedName: currentEmbed,
        user: state.user as User | null | undefined,
      });
      console.debug(res);
    });
  }
});

const signUpParams = computed(() => {
  const returnPath = router.resolve({
    name: appRoutes.share.name,
    params: { uuid: electionStore.resultsId },
  }).path;

  return {
    name: appRoutes.register.name,
    params: {
      ...route.params,
    },
    query: {
      returnPath,
      answerId: electionStore.resultsId,
      updateToken: electionStore.resultsUpdateToken,
    },
  };
});

const signUpPath = computed(() => {
  return router.resolve(signUpParams.value).fullPath;
});

console.debug(encodeResults(electionStore.answers));

const candidateAnswers: DeprecatedCandidateAnswer[] =
  electionStore.calculator?.answers || [];

const hasAllCandidatesInactive =
  electionStore.calculator?.candidates.filter(
    (candidate) => !candidate.is_active,
  ).length === electionStore.calculator?.candidates.length;

const hasActiveCandidatesBtn = hasAllCandidatesInactive
  ? false
  : electionStore.calculator?.candidates.some((x) => !x.is_active);

const showNotActiveCandidates = ref(false);
const filteredCandidateAnswers: Ref<DeprecatedCandidateAnswer[]> =
  ref(candidateAnswers);
const handleActiveCandidatesClicked = (isActive: boolean) => {
  showNotActiveCandidates.value = isActive;
  if (!hasAllCandidatesInactive && !showNotActiveCandidates.value) {
    filteredCandidateAnswers.value = filteredCandidateAnswers.value.filter(
      (x) => {
        return electionStore.calculator?.candidates.find(
          (cnd) => x.candidate_id === cnd.id && cnd.is_active,
        );
      },
    );
  } else if (electionStore.calculator?.answers) {
    filteredCandidateAnswers.value = candidateAnswers;
  }
};
handleActiveCandidatesClicked(false);

const resultsGeneral = computed(() => {
  const ra = calculateRelativeAgreement(
    filteredCandidateAnswers.value,
    electionStore.answers,
  );
  return ra;
});

// Define a type for resultMap with string keys and number values
type ResultMap = {
    [key: string]: number | undefined; // Use undefined to handle cases where a cId might not exist.
};

// Create a map to hold cId and corresponding result_percent
const resultMap: ResultMap = resultsGeneral.value.reduce<ResultMap>((map, e) => {
    if (e.result) {
        map[e.cId] = e.result.result_percent;
    }
    return map;
}, {});

// Retrieve the result_percent for the specified cIds
const ra_kozos = resultMap['d578d28c-dbac-4bae-9cc4-963b506e0101'];
const ra_15min = resultMap['7a6f9a15-2e71-4bca-a45d-94680f9b4755'];
const ra_fent = resultMap['94b53e83-7875-4c16-9ccf-4becae64f089'];
const ra_tech = resultMap['1a93946b-27ba-4fd2-a05b-6474b276815c'];
const ra_auto = resultMap['df6eee27-f75d-430b-bc22-dc3cafa2bc90'];
const ra_gazd = resultMap['1ad707e9-a9c8-4e92-a244-00e156ad25a2'];

const shareModal = ref<InstanceType<typeof ResultShareModal> | null>(null);

// Temporary subscribe
const email = ref('');
const emailError = ref();
const posting = ref();
const success = ref();
const message = ref();

onMounted(() => {
  if (districtCode.includes('english')) {
    switchLanguage('en');
  }
});

onUnmounted(() => {
  switchLanguage(import.meta.env.VITE_DEFAULT_LOCALE);
});
</script>
<template>
  <BackgroundComponent :is-image="false">
    <StickyHeaderLayout>
      <template #header>
        <NavigationBar>
          <template #title>{{ breadcrumbs }}</template>
          <template #right>
            <EmbedWrapper>
              <ResponsiveWrapper medium large extra-large huge>
                <ButtonComponent
                  kind="link"
                  @click="
                    router.push({
                      name: appRoutes.index.name,
                      query: { ...route.query },
                    })
                  "
                >
                  {{ $t('routes.result.ResultPage.back-to-main-page') }}
                  <template #iconAfter>
                    <IconComponent :icon="mdiCloseCircleOutline" />
                  </template>
                </ButtonComponent>
              </ResponsiveWrapper>
              <ResponsiveWrapper extra-small small>
                <ButtonComponent
                  kind="link"
                  @click="
                    router.push({
                      name: appRoutes.index.name,
                      query: { ...route.query },
                    })
                  "
                >
                  <template #icon>
                    <IconComponent
                      :icon="mdiCloseCircleOutline"
                      :title="$t('routes.result.ResultPage.back-to-main-page')"
                    />
                  </template>
                </ButtonComponent>
              </ResponsiveWrapper>
            </EmbedWrapper>
          </template>
        </NavigationBar>
      </template>
      <template #sticky-header>
        <ResponsiveWrapper extra-small small>
          <SecondaryNavigationBar centered-title>
            <template #before>
              <IconButton @click="handlePreviousClick">
                <IconComponent
                  :icon="mdiArrowLeft"
                  :title="$t('routes.result.ResultPage.recapitulation')"
                />
              </IconButton>
            </template>
            <TitleText tag="h2" size="medium">{{
              $t('routes.result.ResultPage.my-match')
            }}</TitleText>
          </SecondaryNavigationBar>
        </ResponsiveWrapper>
        <ResponsiveWrapper medium large extra-large huge>
          <SecondaryNavigationBar>
            <template #before>
              <IconButton @click="handlePreviousClick">
                <IconComponent
                  :icon="mdiArrowLeft"
                  :title="$t('routes.result.ResultPage.recapitulation')"
                />
              </IconButton>
            </template>
            <TitleText tag="h2" size="large">{{
              $t('routes.result.ResultPage.my-match')
            }}</TitleText>
            <template #after>
              <div class="navbar-btn-wrapper">
                <ButtonComponent
                  class="desktop"
                  kind="filled"
                  color="primary"
                  @click="handleShowComparsionClick"
                >
                  {{ $t('routes.result.ResultPage.compare-answers') }}
                  <template #iconAfter>
                    <IconComponent :icon="mdiArrowRight" />
                  </template>
                </ButtonComponent>
              </div>
            </template>
          </SecondaryNavigationBar>
        </ResponsiveWrapper>
      </template>
      <BottomBarWrapper>
        <StackComponent
          v-if="electionStore.answerCount > 0"
          class="main"
          spacing="medium"
        >
          <CheckboxComponent
            v-if="hasActiveCandidatesBtn"
            group-name="test"
            @update:check="handleActiveCandidatesClicked"
          >
            {{
              $t('routes.result.ResultPage.display-not-advancing-candidates')
            }}
          </CheckboxComponent>
          <ButtonComponent
                  class="desktop"
                  kind="filled"
                  color="primary"
                  @click="goToForm"
                >
                <div
                style="white-space: normal;display: inline-block;"
                >
                Miskolci vagy? Vegyél részt a személyes párbeszédben!
                </div>
                  <template #iconAfter>
                    <IconComponent :icon="mdiArrowDown" />
                  </template>
          </ButtonComponent>
          <ResultCategory
            :result="resultsGeneral"
            category="general"
            :max-visible-candidates="6"
          />
          <a name="jelentkezes" href="#jelentkezes">
          <TitleText tag="p" size="medium">Jelentkezés</TitleText>
          </a>

          <div id="framediv" class=".card .card--shadow .card--border-normal">
            <iframe allowtransparency="true" style="background: #FFF;"
              :src="`https://docs.google.com/forms/d/e/1FAIpQLSeMvM2hQqN7kH8UmS0bSXQcu-7bSNHn9i3GDKWfmpYBPsPoHA/viewform?usp=pp_url&entry.584894938=${ra_kozos}&entry.1510674861=${ra_15min}&entry.276333858=${ra_fent}&entry.2052211534=${ra_tech}&entry.2053574064=${ra_auto}&entry.632598064=${ra_gazd}`" 
              width="100%" 
              height="743" 
              frameborder="0" 
              marginheight="0" 
              marginwidth="0"
            ></iframe>
          </div>
        </StackComponent>
        <StackComponent v-else class="main" spacing="medium">
          <CardComponent corner="bottom-left">
            <StackComponent spacing="medium">
              <TitleText tag="p" size="medium">
                {{ $t('routes.result.ResultPage.text-at-least-one-answer') }}
              </TitleText>
              <BodyText tag="p" size="medium">
                {{ $t('routes.result.ResultPage.you-may') }}
                <a
                  :href="
                    router.resolve({
                      name: appRoutes.question.name,
                      params: { ...route.params, nr: 1 },
                      query: { ...route.query },
                    }).path
                  "
                  @click.prevent="handleStartClick"
                  >{{ $t('routes.result.ResultPage.back-to-start') }}</a
                >
                {{ $t('routes.result.ResultPage.text-and-answer') }}
                <a
                  :href="
                    router.resolve({
                      name: appRoutes.comparison.name,
                      params: { ...route.params },
                      query: { ...route.query },
                    }).path
                  "
                  @click.prevent="handleShowComparsionClick"
                >
                  {{ $t('routes.result.ResultPage.text-display-answers') }} </a
                >.
              </BodyText>
              <StackComponent horizontal spacing="medium">
                <ButtonComponent
                  kind="outlined"
                  color="primary"
                  @click="handleStartClick"
                >
                  {{ $t('routes.result.ResultPage.fill-calc') }}
                  <template #iconAfter>
                    <IconComponent :icon="mdiArrowRight" />
                  </template>
                </ButtonComponent>
                <ButtonComponent
                  kind="outlined"
                  color="primary"
                  @click="handleShowComparsionClick"
                >
                  {{ $t('routes.result.ResultPage.candidates-answers') }}
                  <template #iconAfter>
                    <IconComponent :icon="mdiArrowRight" />
                  </template>
                </ButtonComponent>
              </StackComponent>
            </StackComponent>
          </CardComponent>
        </StackComponent>
        <template #bottom-bar>
          <ResponsiveWrapper
            extra-small
            small
          >
            <BottomBar>
              <div class="bottom-bar-grid">
                <ButtonComponent
                  kind="filled"
                  color="primary"
                  @click="handleShowComparsionClick"
                >
                  {{ $t('routes.result.ResultPage.compare-answers') }}
                  <template #iconAfter>
                    <IconComponent :icon="mdiArrowRight" />
                  </template>
                </ButtonComponent>
              </div>
            </BottomBar>
          </ResponsiveWrapper>
        </template>
      </BottomBarWrapper>
    </StickyHeaderLayout>
  </BackgroundComponent>
  <ResultShareModal
    v-if="electionStore.resultsId"
    ref="shareModal"
    :relative-agreement="resultsGeneral"
  />
  <ErrorModal
    v-else
    ref="shareModal"
    :title="$t('routes.result.ResultPage.something-went-wrong')"
  >
    {{ $t('routes.result.ResultPage.something-went-wrong-text') }}
  </ErrorModal>
</template>

<style lang="scss" scoped>
iframe {
}

#framediv {
  // background-color: rgb(var(--color-neutral-bg-container));
  --7b38ec86-border\.width: var(--responsive-border-thin);
  --7b38ec86-border\.radius: var(--responsive-radius-small);
  --7b38ec86-padding\.vertical: calc(var(--responsive-gap-medium) - var(--responsive-border-thin));
  --7b38ec86-padding\.horizontal: calc(var(--responsive-gap-medium) - var(--responsive-border-thin));
  box-shadow: 6px 8px 0px 0px rgba(var(--color-neutral-shadow), var(--transparency-20));
  border-color: rgb(var(--color-neutral-border));
  border-style: solid;
  border-width: var(--7b38ec86-border\.width);
  border-radius: var(--7b38ec86-border\.radius);
  padding-top: var(--7b38ec86-padding\.vertical);
  padding-right: var(--7b38ec86-padding\.horizontal);
  padding-bottom: var(--7b38ec86-padding\.vertical);
  padding-left: var(--7b38ec86-padding\.horizontal);
  padding: 4px;
  // background: #f6f6f6;
  background-color: rgb(252, 234, 234);
}

.navbar-btn-wrapper {
  display: flex;
  flex-direction: row;
  gap: var(--spacing-small);
}
.results-header-note {
  text-align: center;
}
.results-footer-note {
  text-align: center;
}
.main {
  display: grid;
  grid-template-columns: clamp(32rem, 50vw, 48rem);
  justify-content: center;
  padding: var(--spacing-small);
}

/* TODO: update breakpoint */
@media (max-width: 700px) {
  .main {
    grid-template-columns: 1fr;
  }
}

.bottom-bar-grid {
  display: grid;
  grid-template-columns: 1fr;
}
</style>
