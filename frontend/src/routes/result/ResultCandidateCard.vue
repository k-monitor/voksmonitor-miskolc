<script setup lang="ts">
import { ref } from 'vue';
import { mdiChevronUp, mdiChevronDown } from '@mdi/js';
import { useRoute, useRouter } from 'vue-router';
import { appRoutes } from '@/main';

import { useElectionStore } from '@/stores/electionStore';
import {
  avatarsConfiguration,
  type TTopics,
} from '../../components/design-system/configurations/avatars-configuration';
import CardComponent from '@/components/design-system/containers/CardComponent.vue';
import BodyText from '../../components/design-system/typography/BodyText.vue';
import TitleText from '../../components/design-system/typography/TitleText.vue';
import IconButton from '../../components/design-system/input/IconButton.vue';
import DividerComponent from '../../components/design-system/containers/DividerComponent.vue';
import ResultCardContacts from './ResultCardContacts.vue';
import SimpleProgress from '../../components/design-system/indicators/SimpleProgress.vue';
import IconComponent from '../../components/design-system/icons/IconComponent.vue';
import ButtonComponent from '@/components/design-system/input/ButtonComponent.vue';

import AvatarComponent from '@/components/design-system/other/AvatarComponent.vue';

import { useI18n } from 'vue-i18n';

export interface ResultCandidateCardProps {
  order: number;
  canidateId: string;
  result: number;
  strong: boolean;
  category: TTopics;
  expert: boolean;
}

const candidates = {
  'd578d28c-dbac-4bae-9cc4-963b506e0101': 'kozossegi-kozlekedes',
  '7a6f9a15-2e71-4bca-a45d-94680f9b4755': '15-perces-varos',
  '94b53e83-7875-4c16-9ccf-4becae64f089': 'fenntarthato-varos',
  '1a93946b-27ba-4fd2-a05b-6474b276815c': 'hi-tech-varos',
  'df6eee27-f75d-430b-bc22-dc3cafa2bc90': 'autokozpontu-varos',
  '1ad707e9-a9c8-4e92-a244-00e156ad25a2': 'regios-gazdasagi-kozpont',
}

const { t, locale } = useI18n();

const props = defineProps<ResultCandidateCardProps>();
const store = useElectionStore();
const candidate = store.calculator?.candidates.find(
  (x) => x.id === props.canidateId,
);
let avatarConfig = avatarsConfiguration.general;
let primaryColor = '--palette-primary-50';
const router = useRouter();
const route = useRoute();

switch (props.category) {
  case 'environment':
    avatarConfig = avatarsConfiguration.environment;
    primaryColor = '--palette-green-50';
    break;
  case 'health':
    avatarConfig = avatarsConfiguration.health;
    primaryColor = '--palette-red-50';
    break;
  default:
    break;
}

const candidateKey = props.canidateId as keyof typeof candidates;
const candidateName = candidates[candidateKey] || '';

const isExpanded = ref(false);
const toggleClick = () => {
  isExpanded.value = !isExpanded.value;
};
</script>
<template>
  <CardComponent
    :class="[
      'result-question-card',
      isExpanded && 'result-question-card--expanded',
    ]"
    corner="top-left"
    border
    shadow
    padding="medium"
    @click="toggleClick"
  >
    <div class="avatar desktop">
      <AvatarComponent
        :size="order === 1 ? 'extra-large' : 'large'"
        :background-color="
          order === 1
            ? 'rgb(var(--palette-primary-50))'
            : 'rgb(var(--palette-primary-90))'
        "
        :background-image="
          candidate?.img_url ||
          (candidate?.parties?.length === 1
            ? candidate?.parties[0].img_url
            : undefined)
        "
      >
        <BodyText
          :size="order === 1 ? 'large' : 'medium'"
          :color="
            order === 1
              ? 'rgb(var(--color-neutral-fg-inverse))'
              : 'rgb(var(--color-neutral-fg))'
          "
        >
          <strong>{{ order }}.</strong>
        </BodyText>
      </AvatarComponent>
    </div>
    <div class="avatar mobile">
      <AvatarComponent
        :size="order === 1 ? 'medium' : 'small'"
        :background-color="
          order === 1
            ? 'rgb(var(--palette-primary-50))'
            : 'rgb(var(--palette-primary-90))'
        "
        :background-image="
          candidate?.img_url ||
          (candidate?.parties?.length === 1
            ? candidate?.parties[0].img_url
            : undefined)
        "
      >
        <BodyText
          :size="order === 1 ? 'medium' : 'small'"
          :color="
            order === 1
              ? 'rgb(var(--color-neutral-fg-inverse))'
              : 'rgb(var(--color-neutral-fg))'
          "
        >
          <strong>{{ order }}.</strong>
        </BodyText>
      </AvatarComponent>
    </div>
    <div class="text">
      <TitleText class="desktop" tag="p" :size="strong ? 'medium' : 'small'">
        {{ candidate?.short_name }}
      </TitleText>
      <BodyText class="mobile" tag="p" :size="strong ? 'medium' : 'small'">
        <strong>{{ candidate?.short_name }}</strong>
      </BodyText>
    </div>
    <div class="progress-bar">
      <SimpleProgress
        :id="candidate?.id || ''"
        :color-primary="`rgb(var(${primaryColor}))`"
        color-secondary="rgb(var(--color-neutral-bg))"
        height="0.375rem"
        :value="result"
        :max="100"
      ></SimpleProgress>
    </div>
    <div class="toggle">
        <IconComponent
          :icon="isExpanded ? mdiChevronUp : mdiChevronDown"
          size="medium"
          :title="$t('routes.recap.RecapQuestionCard.display-details')"
        />
    </div>
    <StackComponent
      v-show="isExpanded"
      class="expansion"
      spacing="small"
      spacing-responsive
    >
      <BodyText size="medium">{{ "Részletes leírás, képek, mindenféle jóság." }}</BodyText>
      <div class="button-container">
        <ButtonComponent
                    kind="filled"
                    color="primary"
                    @click="
                      router.push({
                        path: '/jovokepek/'+candidateName,
                        query: { },
                      })
                    "
                  >
                  Bővebben
        </ButtonComponent>
      </div>
    </StackComponent>

    <div class="secondary-text">
      <div class="party-wrapper">
        <BodyText v-if="!expert" size="medium">{{
          candidate?.type == 'person' &&
          candidate?.parties &&
          candidate?.parties.length > 0
            ? candidate?.parties?.[0].name
            : candidate?.name
        }}</BodyText>
        <BodyText size="medium" v-if="expert">
          Közforrásokból származó adatok
        </BodyText>
      </div>
    </div>
    <TitleText
      class="percentage desktop"
      tag="p"
      :size="order === 1 ? 'large' : 'medium'"
    >
      {{ result }}&nbsp;%
    </TitleText>
    <TitleText
      class="percentage mobile"
      tag="p"
      :size="order === 1 ? 'medium' : 'small'"
    >
      {{ result }}&nbsp;%
    </TitleText>
    <div v-if="candidate?.motto" class="toggle">
      <IconButton @click="toggleClick">
        <IconComponent
          :icon="isExpanded ? mdiChevronUp : mdiChevronDown"
          size="medium"
          :title="$t('routes.result.ResultCandidateCard.display-details')"
        />
      </IconButton>
    </div>
    <div
      v-if="candidate?.motto || candidate?.contact"
      v-show="isExpanded"
      class="expansion"
    >
      <div v-if="candidate?.motto">
        <BodyText class="motto-title" size="small"
          ><strong>{{
            $t('routes.result.ResultCandidateCard.what-candidate-say')
          }}</strong></BodyText
        >
        <BodyText size="small">{{ candidate?.motto }}</BodyText>
      </div>
      <div v-if="candidate?.contact">
        <DividerComponent class="divider"></DividerComponent>
        <ResultCardContacts :contact="candidate?.contact"></ResultCardContacts>
      </div>
    </div>
  </CardComponent>
</template>

<style lang="scss" scoped>

.button-container {
  display: flex;
  justify-content: flex-end; /* Aligns the button to the right */
  padding: 4px;
}

.motto-title {
  margin-bottom: var(--responsive-spacing-extra-small);
}
.divider {
  margin-bottom: var(--responsive-spacing-extra-small);
  margin-top: var(--responsive-spacing-extra-small);
  margin-left: 0px;
  margin-right: 0px;
}
.party-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  .party {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    gap: var(--responsive-spacing-extra-small);
    .party-logo {
      height: var(--responsive-spacing-medium);
      width: var(--responsive-spacing-medium);
      object-fit: cover;
    }
  }
}

.result-question-card:hover {
  -webkit-filter: brightness(97%);
  filter: brightness(97%);
}

.result-question-card {
  cursor: pointer;
  max-width: 100%;
  display: grid;
  // grid-template-columns: 4.5rem 1fr 4.5rem auto;
  grid-template-areas:
    'avatar text percentage toggle'
    'avatar progress-bar percentage toggle'
    'avatar secondary-text percentage toggle';
  grid-template-columns: 2fr 10fr 2fr 1fr;

  column-gap: var(--responsive-spacing-medium);
  row-gap: var(--responsive-spacing-small);

  .avatar {
    grid-area: avatar;
    align-self: center;
    justify-self: right;
  }

  .text {
    overflow-wrap: break-word;
    word-wrap: break-word;
    word-break: break-word;
    grid-area: text;
    justify-self: stretch;
  }

  .progress-bar {
    grid-area: progress-bar;
    justify-self: stretch;
  }

  .secondary-text {
    grid-area: secondary-text;
    justify-self: left;
  }

  .percentage {
    grid-area: percentage;
    align-self: center;
    justify-self: right;
  }

  .toggle {
    grid-area: toggle;
    align-self: center;
    justify-self: right;
  }

  .expansion {
    grid-area: expansion;
  }

  &--expanded {
    grid-template-areas:
      'avatar text percentage toggle'
      'avatar progress-bar percentage toggle'
      'avatar secondary-text percentage toggle'
      'expansion expansion expansion expansion';

    .expansion {
      margin-top: var(--responsive-spacing-medium);
    }
  }

  @media (max-width: 700px) {
    grid-template-columns: 3rem 1fr 4.5rem auto;
    column-gap: var(--responsive-spacing-extra-small);

    &--expanded {
      row-gap: var(--responsive-spacing-small);
    }
  }

  .desktop,
  .mobile {
    display: none;
  }

  @media (min-width: 700px) {
    .desktop {
      display: initial;
    }
  }

  @media (max-width: 700px) {
    .mobile {
      display: initial;
    }
  }
}
</style>
