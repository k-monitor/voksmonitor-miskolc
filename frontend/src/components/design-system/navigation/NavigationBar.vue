<script setup lang="ts">
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { appRoutes } from '@/main';

import AvatarComponent from '@/components/design-system/other/AvatarComponent.vue';
import ButtonComponent from '@/components/design-system/input/ButtonComponent.vue';
import ContainerComponent from '@/components/design-system/containers/ContainerComponent.vue';
import StackComponent from '@/components/design-system/layout/StackComponent.vue';
import LogoComponent from '@/components/design-system/style/LogoComponent.vue';
import BodyText from '@/components/design-system/typography/BodyText.vue';

import EmbedWrapper from '@/components/utilities/embedding/EmbedWrapper.vue';
import ResponsiveWrapper from '@/components/utilities/ResponsiveWrapper.vue';

import type { User } from '@/stores/userStore';

import { useI18n } from 'vue-i18n';

export interface Props {
  padding?: 'small' | 'medium' | 'large';
  paddingResponsive?: boolean;
  transparent?: boolean;
  centeredTitle?: boolean;
  user?: User | null;
  withAccount?: boolean;
  withLogo?: boolean;
}

const { t, locale } = useI18n();

const props = withDefaults(defineProps<Props>(), {
  padding: 'large',
  paddingResponsive: true,
  transparent: false,
  centeredTitle: false,
  user: undefined,
  withLogo: true,
});

const indexPage = computed(() => useRoute()?.path === '/');

const classes = computed(() => ({
  'navigation-bar--centered-title': props.centeredTitle,
}));

const background = computed(() =>
  props.transparent ? 'transparent' : undefined,
);

const router = useRouter();

const handleRegisterClick = () => router.push(appRoutes.register);

const handleLoginClick = () => router.push(appRoutes.login);
const handleAvatarClick = () => router.push(appRoutes.profile);
</script>

<template>
  <ContainerComponent
    :class="['navigation-bar', classes]"
    :background="background"
    :padding="padding"
    :padding-responsive="paddingResponsive"
  >
    <div v-if="withLogo" class="logo">
      <EmbedWrapper>
        <ResponsiveWrapper extra-small small>
          <LogoComponent :text="false" :link="!indexPage" />
        </ResponsiveWrapper>
        <ResponsiveWrapper medium large extra-large huge>
          <LogoComponent :link="!indexPage" />
        </ResponsiveWrapper>
      </EmbedWrapper>
      <EmbedWrapper embed>
        <ResponsiveWrapper extra-small small>
          <LogoComponent
            :text="false"
            monochromatic="rgb(var(--color-neutral-fg))"
          />
        </ResponsiveWrapper>
        <ResponsiveWrapper medium large extra-large huge>
          <LogoComponent monochromatic="rgb(var(--color-neutral-fg))" />
        </ResponsiveWrapper>
      </EmbedWrapper>
    </div>
    <ResponsiveWrapper extra-small>
      <div class="title">
        <BodyText size="extra-small">
          <slot name="title" />
        </BodyText>
      </div>
    </ResponsiveWrapper>
    <ResponsiveWrapper small>
      <div class="title title--centered">
        <BodyText size="small">
          <slot name="title" />
        </BodyText>
      </div>
    </ResponsiveWrapper>
    <ResponsiveWrapper medium large extra-large huge>
      <div class="title">
        <BodyText size="small">
          <slot name="title" />
        </BodyText>
      </div>
    </ResponsiveWrapper>
    <StackComponent
      class="right"
      horizontal
      spacing="medium"
      spacing-responsive
    >
      <slot name="right">
        <BodyText size="small">
          <a href="https://adatbazis.k-monitor.hu/egyeb/adatkezelesi-tajekoztato" target="_blank">Adatkezelési tájékoztató</a>
        </BodyText>
        <BodyText size="small">
          <a href="/about">A projektről</a>
        </BodyText>
        <AvatarComponent
          v-if="withAccount && user"
          size="small"
          background-color="rgb(var(--palette-primary-90))"
          :name="user.displayName ? user.displayName : user.email"
          class="user-avatar"
          @click="() => handleAvatarClick()"
        />
        <StackComponent
          v-if="withAccount && !user"
          class="right"
          horizontal
          centered
          spacing="medium"
        >
          <!-- <ResponsiveWrapper medium large extra-large huge>
            <ButtonComponent kind="link" @click="handleRegisterClick">{{
              $t(
                'components.design-system.navigation.NavigationBar.create-account',
              )
            }}</ButtonComponent>
            <ButtonComponent
              kind="outlined"
              size="small"
              @click="handleLoginClick"
              >{{
                $t('components.design-system.navigation.NavigationBar.login')
              }}</ButtonComponent
            >
          </ResponsiveWrapper>
          <ResponsiveWrapper extra-small small>
            <ButtonComponent
              kind="link"
              color="primary"
              size="small"
              @click="handleLoginClick"
            ></ButtonComponent>
          </ResponsiveWrapper> -->
        </StackComponent>
      </slot>
    </StackComponent>
  </ContainerComponent>
</template>

<style scoped lang="scss">
.navigation-bar {
  display: grid;
  grid-template-columns: auto auto 1fr;
  grid-template-areas: 'logo title right';
  align-items: center;
  gap: var(--responsive-spacing-large);
  width: 100%;

  .logo {
    grid-area: logo;
  }

  .title {
    grid-area: title;

    &--centered {
      grid-column-start: logo;
      grid-column-end: right;
      justify-self: center;
    }
  }

  .right {
    grid-area: right;
    justify-content: end;
  }
}

.user-avatar {
  cursor: pointer;
}
</style>
