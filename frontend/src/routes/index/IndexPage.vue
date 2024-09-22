<script setup lang="ts">
import { computed, ref, onMounted, onUnmounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import {
  mdiCloseCircleOutline,
  mdiArrowRight,
  mdiArrowLeft,
  mdiFastForward,
} from '@mdi/js';

import { appRoutes } from '@/main';
import { useElectionStore } from '@/stores/electionStore';

import type { DeprecatedElection } from '@/types/election';

import BackgroundComponent from '@/components/design-system/style/BackgroundComponent.vue';
import BodyText from '@/components/design-system/typography/BodyText.vue';
import BottomBar from '@/components/design-system/navigation/BottomBar.vue';
import BottomBarWrapper from '@/components/design-system/layout/BottomBarWrapper.vue';
import ButtonComponent from '@/components/design-system/input/ButtonComponent.vue';
import CardComponent from '@/components/design-system/containers/CardComponent.vue';
import HeadingComponent from '@/components/design-system/typography/HeadingComponent.vue';
import IconButton from '@/components/design-system/input/IconButton.vue';
import IconComponent from '@/components/design-system/icons/IconComponent.vue';
import LabelText from '@/components/design-system/typography/LabelText.vue';
import NavigationBar from '@/components/design-system/navigation/NavigationBar.vue';
import SecondaryNavigationBar from '@/components/design-system/navigation/SecondaryNavigationBar.vue';
import StackComponent from '@/components/design-system/layout/StackComponent.vue';
import StepProgress from '@/components/design-system/other/StepProgress.vue';
import StepWrapper from '@/components/design-system/layout/StepWrapper.vue';
import HeadlineText from '@/components/design-system/typography/HeadlineText.vue';

import {
  vkiLogoInFavour,
  vkiLogoAgainst,
  vkiLogoNeutral,
  vkiStarOutlined,
  vkiStarFilled,
} from '@/components/design-system/icons';

import EmbedWrapper from '@/components/utilities/embedding/EmbedWrapper.vue';
import MarkdownIt from '@/components/utilities/MarkdownIt.vue';
import ResponsiveWrapper from '@/components/utilities/ResponsiveWrapper.vue';
import StickyHeaderLayout from '@/components/layouts/StickyHeaderLayout.vue';
import { getDistrictCode } from '@/common/utils';

import { useI18n } from 'vue-i18n';
import { switchLanguage } from '@/i18n';

const { t, locale } = useI18n();

const router = useRouter();
const route = useRoute();
const electionStore = useElectionStore();

const election = electionStore.election as DeprecatedElection;
const electionName = election.name;
const croute = router.resolve('/valasztasok/parkolasi-jovokepek/voksmonitor/utmutato');
const districtCode = getDistrictCode(croute.params.second as string);
const districtName = electionStore.districts.filter(
  (district) => district.district_code === districtCode,
)[0].name;
const showDistrictCode = electionStore.districts.filter(
  (district) => district.district_code === districtCode,
)[0].show_district_code;
const districtNameWithCode = showDistrictCode
  ? `${districtName} (${districtCode})`
  : districtName;

const breadcrumbs = `${electionName}`;

// TODO: Replace with data from store
// const text =
//   route.params.first === 'senatni-2022'
//     ? `
// Vítejte ve Volební kalkulačce pro volby do Senátu ČR.

// Čeká vás zhruba 40 otázek. Na stejné otázky nám odpověděli kandidáti. Zodpovězení otázek zabere cca 10 minut. Na konci se dozvíte, jak se kandidáti shodují s vašimi názory.
//       `
//     : route.params.first === 'prezidentske-2023' &&
//       route.params.second === 'pro-kazdeho'
//     ? `
// Vítejte ve Volební kalkulačce pro prezidentské volby 2023.

// Čeká vás 42 otázek. Na stejné otázky nám odpověděly kandidující osobnosti. Zodpovězení otázek zabere zhruba 10 minut. Na konci se dozvíte, jak se jednotliví kandidáti a kandidátky shodují s vašimi názory.
//     `
//     : route.params.first === 'nrsr-2023' &&
//       route.params.second === 'inventura-2020-2023'
//     ? `
// Vitajte v Inventúre hlasovaní Národnej rady SR 2020-2023!

// Vybrali sme pre Vás 30 skutočných hlasovaní, ktoré sa uskutočnili v Národnej rade SR v končiacom volebnom období. Predstavte si, že o nich hlasujete ako jeden z poslancov alebo poslankýň. Zodpovedanie otázok zaberie zhruba 5 minút. Na konci sa dozviete, ktorí poslanci sa zhodovali s vašimi názormi.
//     `
//     : route.params.first === 'prezidentske-2023' &&
//       route.params.second === 'pro-nadsence'
//     ? `
// Vítejte ve Volební kalkulačce pro prezidentské volby 2023.

// Čeká vás 98 otázek. Na stejné otázky nám odpověděly kandidující osobnosti. Zodpovězení otázek zabere zhruba 10 minut. Na konci se dozvíte, jak se jednotliví kandidáti a kandidátky shodují s vašimi názory.
//     `
//     : route.params.first === 'prezidentske-2023' &&
//       route.params.second === 'pro-mlade'
//     ? `
// Volební kalkulačka pro mladé byla vytvořena ve **spolupráci s projektem [NázoryPolitiků.cz](https://www.nazorypolitiku.cz)**.

// Projekt vznikl v roce 2020 jako iniciativa středoškolských studentů. Tým se z původní dvojice rozrostl na **15 studentů, kteří se snaží pomáhat voličům** orientovat se v názorech kandidátů. Za **3 roky** pomohl projekt s rozhodováním více než **100 000 voličů**.

// Na základě průzkumů a po konzultacích se sociology bylo vybráno **16 otázek, které mládež a prvovoliči považují za stěžejní témata** voleb. Naší vizí je přinést věcnost a přehlednost do politiky, zvýšit volební účast a podpořit tak demokracii.
//     `
//     : `
// Vítejte ve Volební kalkulačce pro komunální volby 2022.

// Čeká vás zhruba 40 otázek. Na stejné otázky nám odpověděly kandidující strany. Zodpovězení otázek zabere cca 10 minut. Na konci se dozvíte, jak se kandidující strany shodují s vašimi názory.
//     `;

const text = electionStore.calculator?.intro as string;

const forwardRoute = computed(
  () =>
    router.options.history.state.forward &&
    router.resolve(router.options.history.state.forward as string),
);

const backRoute = computed(
  () =>
    router.options.history.state.back &&
    router.resolve(router.options.history.state.back as string),
);

const stepsCount = 4;
const currentStep = computed(() => parseInt(route.params.step as string) || 1);
const farthestCompletedStep = ref(
  Math.max(
    currentStep.value - 1,
    forwardRoute.value && forwardRoute.value.name === appRoutes.question.name
      ? 4
      : 0,
    backRoute.value && backRoute.value.name === appRoutes.question.name ? 4 : 0,
  ),
);

const previousButtonTitle = computed(() => {
  if (currentStep.value === 1) {
    return t('routes.guide.GuidePage.next-step');
  } else {
    return t('routes.guide.GuidePage.previous-step');
  }
});

const nextButtonTitle = computed(() => {
  if (currentStep.value < stepsCount) {
    return t('routes.guide.GuidePage.next-step');
  } else {
    return t('routes.guide.GuidePage.first-question');
  }
});
const nextButtonKind = computed(() => {
  if (currentStep.value < stepsCount) {
    return 'outlined';
  } else {
    return 'filled';
  }
});
const nextButtonColor = computed(() => {
  if (currentStep.value < stepsCount) {
    return 'neutral';
  } else {
    return 'primary';
  }
});

const skipButtonVisibility = computed(() => {
  if (currentStep.value < stepsCount) {
    return 'initial';
  } else {
    return 'hidden';
  }
});

const goToStep = (number: number) => {
  router.push({
    name: 'cindex',
    params: { ...route.params, step: number },
    query: { ...route.query },
  });
};

const goToQuestions = () => {
  // Initialize store here
  electionStore.init();
  router.push({
    name: 'question',
    params: { ...croute.params, nr: 'first' },
    query: { ...croute.query },
  });
};

const goToDistrictSelection = () => {
  router.push({
    name: 'district-selection',
    params: { ...route.params },
    query: { ...route.query },
  });
};

const handleNextClick = () => {
  farthestCompletedStep.value = Math.max(
    farthestCompletedStep.value,
    currentStep.value,
  );

  if (currentStep.value < stepsCount) {
    goToStep(currentStep.value + 1);
  } else {
    goToQuestions();
  }
};

const handlePreviousClick = () => {
  if (currentStep.value === 1) {
    goToDistrictSelection();
  } else {
    goToStep(currentStep.value - 1);
  }
};

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
        <NavigationBar transparent>
          <template #title>{{ breadcrumbs }}</template>
        </NavigationBar>
      </template>
      <template #sticky-header>
        <ResponsiveWrapper extra-small small>
          <SecondaryNavigationBar transparent>
            <template v-if="currentStep > 1" #before>
              <IconButton @click="handlePreviousClick">
                <IconComponent
                  :icon="mdiArrowLeft"
                  :title="previousButtonTitle"
                />
              </IconButton>
            </template>
            <template v-if="farthestCompletedStep >= currentStep" #after>
              <IconButton @click="handleNextClick">
                <IconComponent :icon="mdiArrowRight" :title="nextButtonTitle" />
              </IconButton>
            </template>
          </SecondaryNavigationBar>
        </ResponsiveWrapper>
      </template>
      <BottomBarWrapper>
        <StepWrapper centered>
          <template #before>
            <ResponsiveWrapper medium large extra-large huge>
              <IconButton v-if="currentStep > 1" @click="handlePreviousClick">
                <IconComponent
                  :icon="mdiArrowLeft"
                  :title="previousButtonTitle"
                />
              </IconButton>
            </ResponsiveWrapper>
          </template>
          <StackComponent v-if="currentStep === 1" spacing="small">
            <HeadingComponent kind="title" size="medium">
              Közlekedési teszt
              <template #secondary
                ><small>Milyen jövőben gondolkodsz?</small></template
              >
            </HeadingComponent>
            <BodyText size="medium">
              2040 még bő másfél évtized! Nem sci-fi távolság, nem lesznek repülő autóink, kiborg komornyikok és csillagközi nyaralásra sem utazhatunk, de a mindennapi életünk így is alaposan megváltozik majd. Képzeljük el a találkozást a 2040-es önmagunkkal. Lesz, aki házasságot kötött, új lakásba költözött és időközben ledobott vagy felszedett néhány kilót. Azt, milyen irányba fordul az életünk, a ma meghozott döntéseink befolyásolják.
            </BodyText>

            <BodyText size="medium">
              És a város ahol élünk, az vajon hogyan változik? Máshogy néznek ki a köztereink? Digitálisan vagy személyesen érintkezünk egymással? Milyenek lesznek a munkahelyek, hol vásárolunk? Komótosabban és több döccenővel, de a városi élet keretei is a benne élő emberek döntései és igényei mentén formálódnak. Épített környezetünk és a közlekedésünk olyan lesz, amilyenné közösen tesszük.
            </BodyText>

            <BodyText size="medium">
              Ez a teszt segít átgondolni, hogy milyen lenne az a város, ami a mostani egyéni választásaink, olykor tudatos, olykor kényelmi alapon kialakított szokásaink szerint fejlődik. Nagyjából 35 gombnyomással kiderítheted, hogyan hat 15 éves időtávon az, ha valamiből többet akarsz, másból kevesebbet az utakon és a köztereken. Tedd próbára, hogyan nézne ki 2040-ben a város, ha annak a te mostani választásaid szabnának irányt!
            </BodyText>

          </StackComponent>
          <StackComponent v-if="currentStep === 2" spacing="small">
            <HeadlineText tag="h3" size="extra-small">Kedves miskolciak!</HeadlineText>
            
            <BodyText size="medium">
              A <a href="https://www.dialogegyesulet.hu/">Dialóg</a>, a <a href="https://k-monitor.hu/">K-Monitor</a> és a <a href="https://jarokelo.hu/">Járókelő</a> szakértői által kidolgozott közlekedési tesztet ti próbálhatjátok ki először! Az oldal a válaszok alapján megmutatja, hogy a hat jövőkép - hat alternatív Miskolc - közül a kitöltő melyikhez áll a legközelebb. Ezek segítenek átgondolni, milyen következményekkel járnak a választásaink, és hogyan függnek össze a városi élettel, közlekedéssel kapcsolatos szakpolitikai döntések.
            </BodyText>

            <BodyText size="medium">
              A teszt nem mond ítéletet a jövőképekről, csupán elgondolkodtatni szeretne arról, milyen városban élünk most és milyenben szeretnénk a jövőben. A víziók nem egymást kizáró fejlődési utak. A valóságban sem összeegyeztethetetlen elképzelések csatáznak egymással, hanem ezek valamilyen ötvözete valósul meg. A városban élő, különböző igényű embereknek közösen, egymással párbeszédben kell kialakítaniuk egy mindenki számára elfogadható irányt.
            </BodyText>

            <BodyText size="medium">
              A kérdőív miskolci kitöltőit ezért egy interaktív fórumra hívjuk, ahol a Dialóg Egyesület szervezésében a különböző jövőképekhez közeli résztvevők megvitathatják, milyen közlekedést szeretnének Miskolcon 2040-ben. Jelentkezz az eseményre a teszt végén!
            </BodyText>
          </StackComponent>
          <StackComponent v-if="currentStep === 3" spacing="small">
            <BodyText size="medium">
              A teszt során 33 állítással kapcsolatban kell kinyilvánítanod az álláspontodat:
            </BodyText>
            <CardComponent
              corner="bottom-right"
              border
              style="align-self: center"
            >
              <StackComponent spacing="small">
                <StackComponent horizontal spacing="small">
                  <IconComponent
                    :icon="vkiLogoInFavour"
                    color="rgb(var(--color-primary-fg))"
                  />
                  <BodyText size="medium"
                    >= {{ "Egyetértek" }}</BodyText
                  >
                </StackComponent>
                <StackComponent horizontal spacing="small">
                  <IconComponent
                    :icon="vkiLogoAgainst"
                    color="rgb(var(--color-secondary-fg))"
                  />
                  <BodyText size="medium"
                    >= {{ "Nem értek egyet" }}</BodyText
                  >
                </StackComponent>
                <StackComponent horizontal spacing="small">
                  <IconComponent
                    :icon="vkiLogoNeutral"
                    color="#333"
                  />
                  <BodyText size="medium"
                    >= {{ "Nem tudom / nem érdekel" }}</BodyText
                  >
                </StackComponent>
              </StackComponent>
            </CardComponent>
            <StackComponent spacing="extra-small">
              <BodyText size="medium">
              Amennyiben a válaszod megegyezik egy jövőképhez rendelt válasszal, az egy pontot ér. Amennyiben ellentétes a válasz, egy pontot levonunk.
            </BodyText>
            <BodyText size="medium">
              Ha nincs álláspontod a témáról, vagy nem szeretnél válaszolni, a Nem tudom / nem érdekel gombra kattintva, vagy a jobb oldalon található nyíllal továbbléphetsz. Amennyiben egy jövőképhez nem tartozik egyértelmű álláspont, vagy te nem foglaltál állást, úgy a választ nem értékeljük.
            </BodyText>
            </StackComponent>
          </StackComponent>
          <StackComponent v-if="currentStep === 4" spacing="small">
            <BodyText size="medium">
              A kérdőív végén áttekintheted és módosíthatod a válaszaidat, és csillaggal jelölheted a számodra fontos témákat. Ezeket a program dupla súllyal veszi számításba.
            </BodyText>
            <!-- TODO: remove inline styles -->
            <CardComponent
              corner="bottom-right"
              border
              style="align-self: center"
            >
              <StackComponent horizontal centered spacing="small">
                <IconComponent :icon="vkiStarOutlined" />
                <IconComponent :icon="mdiArrowRight" size="small" />
                <IconComponent
                  :icon="vkiStarFilled"
                  color="rgb(var(--palette-yellow))"
                />
              </StackComponent>
            </CardComponent>
          </StackComponent>
          <template #after>
            <ResponsiveWrapper medium large extra-large huge>
              <IconButton
                v-if="farthestCompletedStep >= currentStep"
                @click="handleNextClick"
              >
                <IconComponent :icon="mdiArrowRight" :title="nextButtonTitle" />
              </IconButton>
            </ResponsiveWrapper>
          </template>
        </StepWrapper>
        <template #bottom-bar>
          <ResponsiveWrapper medium large extra-large huge>
            <BottomBar class="bottom-bar" transparent>
              <LabelText class="text">
                {{ $t('routes.guide.GuidePage.guide') }}
                {{ currentStep }}&hairsp;/&hairsp;{{ stepsCount }}
              </LabelText>
              <StepProgress class="progress-indicator" :current="currentStep" />
              <ButtonComponent
                class="next-button"
                :kind="nextButtonKind"
                :color="nextButtonColor"
                @click="handleNextClick"
              >
                {{ nextButtonTitle }}
                <template #iconAfter>
                  <IconComponent :icon="mdiArrowRight" />
                </template>
              </ButtonComponent>
              <ButtonComponent
                class="skip-button"
                kind="link"
                @click="goToQuestions"
              >
                {{ $t('routes.guide.GuidePage.skip-guide') }}
                <template #iconAfter>
                  <IconComponent :icon="mdiFastForward" />
                </template>
              </ButtonComponent>
            </BottomBar>
          </ResponsiveWrapper>
          <ResponsiveWrapper extra-small small>
            <BottomBar class="bottom-bar">
              <LabelText class="text">
                {{ $t('routes.guide.GuidePage.guide') }}
                {{ currentStep }}&hairsp;/&hairsp;{{ stepsCount }}
              </LabelText>
              <StepProgress class="progress-indicator" :current="currentStep" />
              <ButtonComponent
                class="next-button"
                :kind="nextButtonKind"
                :color="nextButtonColor"
                @click="handleNextClick"
              >
                {{ nextButtonTitle }}
                <template #iconAfter>
                  <IconComponent :icon="mdiArrowRight" />
                </template>
              </ButtonComponent>
              <ButtonComponent
                class="skip-button"
                kind="link"
                @click="goToQuestions"
              >
                {{ $t('routes.guide.GuidePage.skip-guide') }}
                <template #iconAfter>
                  <IconComponent :icon="mdiFastForward" />
                </template>
              </ButtonComponent>
            </BottomBar>
          </ResponsiveWrapper>
        </template>
      </BottomBarWrapper>
    </StickyHeaderLayout>
  </BackgroundComponent>
</template>

<style lang="scss" scoped>
.bottom-bar {
  display: grid;
  grid-template-columns: repeat(2, 8rem);
  gap: var(--spacing-small);
  justify-content: center;

  /* TODO: update breakpoint */
  @media (max-width: 700px) {
    grid-template-columns: repeat(2, 1fr);
  }

  .text {
    grid-column: 1;
    justify-self: start;
  }

  .progress-indicator {
    grid-column: 2;
    justify-self: end;
  }

  .next-button {
    grid-column: 1 / span 2;
    grid-row: 2;
  }

  .skip-button {
    visibility: v-bind(skipButtonVisibility);
    grid-column: 1 / span 2;
    grid-row: 3;
    justify-self: center;
  }
}
</style>
