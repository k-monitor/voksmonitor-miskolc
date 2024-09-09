<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { mdiCloseCircleOutline, mdiArrowLeft } from '@mdi/js';
import { defineStore } from 'pinia';

import { appRoutes } from '@/main';
import { useElectionStore } from '@/stores/electionStore';

import type { DeprecatedElection } from '@/types/election';

import BackgroundComponent from '@/components/design-system/style/BackgroundComponent.vue';
import BodyText from '@/components/design-system/typography/BodyText.vue';
import BottomBar from '@/components/design-system/navigation/BottomBar.vue';
import BottomBarWrapper from '@/components/design-system/layout/BottomBarWrapper.vue';
import ButtonComponent from '@/components/design-system/input/ButtonComponent.vue';
import IconComponent from '@/components/design-system/icons/IconComponent.vue';
import NavigationBar from '@/components/design-system/navigation/NavigationBar.vue';
import RadioButtonComponent from '@/components/design-system/input/RadioButtonComponent.vue';
import SecondaryNavigationBar from '@/components/design-system/navigation/SecondaryNavigationBar.vue';
import StackComponent from '@/components/design-system/layout/StackComponent.vue';
import TitleText from '@/components/design-system/typography/TitleText.vue';
import PillGroupComponent from '@/components/design-system/input/PillGroupComponent.vue';
import PillGroupItemComponent from '@/components/design-system/input/PillGroupItemComponent.vue';

import EmbedWrapper from '@/components/utilities/embedding/EmbedWrapper.vue';
import MarkdownIt from '@/components/utilities/MarkdownIt.vue';
import ResponsiveWrapper from '@/components/utilities/ResponsiveWrapper.vue';
import StickyHeaderLayout from '@/components/layouts/StickyHeaderLayout.vue';
import { stringToNormalizedHyphenated } from '@/common/utils';

const router = useRouter();
const route = useRoute();
const electionStore = useElectionStore();

const election = electionStore.election as DeprecatedElection;
const electionName = election.name;
const electionDescription = election.description;

const breadcrumbs = electionName;

watch(
  () => route.params.election,
  (newElectionKey) => {
    if (newElectionKey) {
      electionStore.setSelectedElectionKey(newElectionKey as string);
    }
  },
  { immediate: true } // Run the callback immediately with the current value
);

const jovokepek = {
  'kozossegi-kozlekedes': { name: "Közösségi közlekedésen alapuló város", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." },
  '15-perces-varos': { name: "15 perces város", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." },
  'fenntarthato-varos': { name: "Fenntartható város", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." },
  'technokrata-varos': { name: "Technokrata város", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." },
  'autokozpontu-varos': { name: "Autóközpontú város", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." },
  'regios-gazdasagi-kozpont': { name : "Régiós gazdasági központ", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." },
};
// const electionKey = route.params.election ;

const title = computed(() => jovokepek[electionStore.selectedElectionKey as keyof typeof jovokepek]?.name || '');
const text = computed(() => jovokepek[electionStore.selectedElectionKey as keyof typeof jovokepek]?.text || '');

const options = electionStore.districts.map((district) => {
  const normalizedName = stringToNormalizedHyphenated(district.name);
  const path = Number(district.district_code)
    ? `${district.district_code}-${normalizedName}`
    : district.district_code;
  return {
    value: path,
    label:
      district.name +
      (district.show_district_code ? ` (${district.district_code})` : ''),
  };
});

const selected = ref((route.params.second as string) || null);

const onSubmit = () => {
  console.debug(selected);
  if (selected.value) {
    router.push({
      name: appRoutes.guide.name,
      params: { ...route.params, second: selected.value, nr: 1 },
      query: { ...route.query },
    });
  }
};
const toggleElection = (key: string) => {
  electionStore.setSelectedElectionKey(key); // Update store with new election
  router.replace({
    path: `/jovokepek/${key}`,
  });
};

</script>

<template>
  <BackgroundComponent :is-image="false">
    <StickyHeaderLayout>
      <template #header>
        <NavigationBar transparent>
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
                  Vissza a főoldalra
                  <template #iconAfter>
                    <IconComponent :icon="mdiCloseCircleOutline" />
                  </template>
                </ButtonComponent>
              </ResponsiveWrapper>
            </EmbedWrapper>
          </template>
        </NavigationBar>
      </template>

      <template #sticky-header>
        <div id="election-selector">
          <ButtonComponent
            kind="link"
            size="medium"
            class="back-button"
            @click="
              router.back()
            "
          >
                <IconComponent
                  :icon="mdiArrowLeft"
                  title="Vissza"
                />
          Vissza
          </ButtonComponent>
        <pill-group-component>
          <pill-group-item-component
            v-for="(value, key) in jovokepek"
            :key="key"
            type="radio"
            :group-name="key"
            :value="key"
            :checked="key === electionStore.selectedElectionKey"
            @click="toggleElection(key)"
            >
            {{
              value.name
            }}
          </pill-group-item-component>
        </pill-group-component>
      </div>
        <ResponsiveWrapper extra-small small>
          <SecondaryNavigationBar transparent centered-title>
            <TitleText tag="h2" size="medium">{{ title }}</TitleText>
          </SecondaryNavigationBar>
        </ResponsiveWrapper>
        <ResponsiveWrapper medium large extra-large huge>
          <SecondaryNavigationBar transparent>
            <TitleText tag="h2" size="large">{{ title }}</TitleText>
          </SecondaryNavigationBar>
        </ResponsiveWrapper>
      </template>
        <BottomBarWrapper>
          <div class="main">
            <BodyText tag="p" size="medium">
              {{ text }}
            </BodyText>
          </div>
        </BottomBarWrapper>
    </StickyHeaderLayout>
  </BackgroundComponent>
</template>

<style lang="scss" scoped>
#election-selector {
  padding-left: 20px;
  display: flex;
  align-items: center;
}

.back-button {
  margin-right: 20px;
}

.main {
  display: grid;
  grid-template-columns: minmax(24rem, max-content);
  justify-content: center;
  align-items: center;
  height: 100%;
  padding: var(--spacing-small);
}

/* TODO: update breakpoint */
@media (max-width: 700px) {
  .main {
    grid-template-columns: 1fr;
  }
}

form {
  display: contents;
}

.bottom-bar {
  display: grid;
  grid-template-columns: max-content;
  justify-content: center;

  @media (max-width: 700px) {
    grid-template-columns: 1fr;
  }
}
</style>
