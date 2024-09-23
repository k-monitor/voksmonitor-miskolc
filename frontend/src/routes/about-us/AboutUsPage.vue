<script setup lang="ts">
import BackgroundComponent from '@/components/design-system/style/BackgroundComponent.vue';
import StickyHeaderLayout from '@/components/layouts/StickyHeaderLayout.vue';
import NavigationBar from '@/components/design-system/navigation/NavigationBar.vue';
import FooterMultiWord from '@/components/FooterMultiWord.vue';
import DonateBlock from '@/components/DonateBlock.vue';
import StaticContentLayout from '@/components/layouts/StaticContentLayout.vue';
import HeadlineText from '@/components/design-system/typography/HeadlineText.vue';
import BodyText from '@/components/design-system/typography/BodyText.vue';
import StackComponent from '@/components/design-system/layout/StackComponent.vue';
import TitleText from '@/components/design-system/typography/TitleText.vue';
import ContainerComponent from '@/components/design-system/containers/ContainerComponent.vue';
import LogoComponent from '@/components/design-system/style/LogoComponent.vue';
import logos from "./logos.png";
</script>

<template>
  <BackgroundComponent>
    <StickyHeaderLayout>
      <template #header>
        <ContainerComponent
          class="navigation-bar"
          padding="medium"
          responsive-padding
          background="transparent"
        >
            <router-link to="/"
              ><LogoComponent responsive />
              <div class="title">
                <BodyText size="small"> </BodyText></div
            ></router-link>
            <slot name="right">
              <StackComponent class="right" horizontal spacing="small">
                <BodyText size="small">
                <a href="https://adatbazis.k-monitor.hu/egyeb/adatkezelesi-tajekoztato">Adatkezelési tájékoztató</a>
              </BodyText>
              <BodyText size="small">
                <a href="/">Teszt</a>
              </BodyText>
            </StackComponent>
          </slot>
          </ContainerComponent>

      </template>
    </StickyHeaderLayout>
    <StaticContentLayout>
      <StackComponent spacing="large" class="section">
        <HeadlineText tag="h1" size="large">A projektről</HeadlineText>
        <BodyText size="large">
          A Közlekedési tesz - Közlekedési jövőképek 2040 oldal a <a href="https://k-monitor.hu/">K-Monitor Egyesület</a> és a <a href="https://www.dialogegyesulet.hu/">Dialóg Egyesület</a> együttműködésében, a Járókelő Közhasznú Egyesület szakértőinek közreműködésével jött létre. Az oldal célja egy nagyváros példáján bemutatni, hogyan befolyásolják a közlekedéspolitikai és a közterek kialakításával kapcsolatos egyéni értékválasztások és elvárások 2040-es időtávon azt, milyen irányba fejlődik a város közlekedése.
        </BodyText>

        <BodyText size="large">
          Az oldalon elérhető teszt segítségével 33 egyéni szinten, saját igényeid és értékítéleted alapján mérlegelhető állításról mondhatod el, hogy egyetértesz-e vele. Ez alapján a K-Monitor <a href="https://voksmonitor.hu/">Voksmonitor</a> alkalmazásának elvén működő teszt megmutatja, hogy a szakértőkkel kidolgozott 6 jövőkép közül melyik és milyen százalékos arányban áll hozzád közel a válaszok alapján.
        </BodyText>
        
        <BodyText size="large">
          <b>A jövőképeket grafikus illusztrációval és részletes leírással <a href="https://kozlekedes2040.hu/jovokepek/kozossegi-kozlekedes">itt böngészheted</a>.</b>
        </BodyText>

        <BodyText size="large">
          A teszt és a hozzá kapcsolódó, személyes párbeszéden alapuló esemény a K-Monitor “<a href="https://k-monitor.hu/tevekenysegek/20240124-kozosen-monitorozunk">Közösen monitorozunk!</a>” projektjének keretében valósul meg. A projekt célja a helyi demokrácia erősítése és a lokális szakpolitikai kérdésekről folytatott diskurzusok támogatása, a projektben résztvevők tény- és adatalapú érdekvédelmi kompetenciáinak fejlesztése, illetve a helyi közügyek sajtóreprezentációjával kapcsolatos partnerségek és tudatosság erősítése. A projektben a K-Monitor és vidéki partnerszervezetei olyan online eszközöket próbálnak ki, mint a Voksmonitor, a <a href="https://kozertheto.k-monitor.hu/">Közérthető Költségvetés</a> vagy a <a href="https://partimap.eu/">PARTIMAP</a> térképes kérdőív.
        </BodyText>

        <BodyText size="large">
          A projekt az Európai Unió "Polgárok, egyenlőség, jogok és értékek” (CERV) programjának támogatásával, a <a href="https://kozosertekeink.hu/">Közös Értékeink</a> program keretében valósul meg. A program lebonyolítói: <a href="https://okotars.hu/">Ökotárs Alapítvány</a> ; <a href="https://autonomia.hu/hu">Autonómia Alapítvány</a> ; <a href="https://karpatokalapitvany.hu/">Kárpátok Alapítvány-Magyarország</a> ; <a href="https://kofe.hu/">Közösségfejlesztők Egyesülete</a>.
        </BodyText>

        <BodyText size="large">
          Az Európai Bizottság támogatása nem jelenti a projektben megvalósított tevékenységek tartalmának jóváhagyását, amely kizárólag az azt megvalósítók álláspontját tükrözi, valamint a Bizottság nem tehető felelőssé ezen információk bárminemű felhasználásáért.
        </BodyText>

        <img class="k-monitor-logo" :src=logos />
      </StackComponent>
    </StaticContentLayout>
  </BackgroundComponent>
</template>

<style lang="scss" scoped>
.section {
  padding: 40px 0;
}
img {
  width: 100%;
}
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
