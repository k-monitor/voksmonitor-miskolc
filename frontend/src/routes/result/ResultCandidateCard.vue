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
// import markdownIt from 'markdown-it';
import MarkdownIt from '@/components/utilities/MarkdownIt.vue';

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

const candidatesText = {
  'd578d28c-dbac-4bae-9cc4-963b506e0101': '<p>2040-re az egymást követő városvezetések egyetértésével egy fejlett, vonzó és megfizethető közösségi közlekedési rendszer jött létre a városban. Ez kulcsszerepet játszott nemcsak a közlekedési problémák megoldásában, de a lakosság életminőségének javításában is. A rendszer nem csupán csökkentette az egyéni autóhasználatot és a közterületi parkolást, de hozzájárult a városi közterületek élhetőbbé és biztonságosabbá tételéhez is, mérsékelve a közúti forgalom negatív környezeti és társadalmi hatásait. A módszeres, tervszerű, felülről vezérelt átalakítás eredményeként közösségi közlekedéssel és ahhoz kapcsolódóan gyalogosan és mikromobilitási eszközökkel könnyen elérhetőek a lakóövezetek, bevásárlóutcák és szolgáltató központok. A pozitív hatások hasonló mértékben érintették a legtöbb városrész lakóját. A lassú de stabil növekedésre építve a város gazdasága több lábon áll, ami az alacsony közlekedési költségek mellett biztos megélhetést teremt a legtöbb városlakónak.</p><br><p>A közösségi közlekedésen alapuló város jövőképe ugyanakkor ingatag egyensúlyt valósít meg, hiszen a rendszer folyamatos fejlesztése az önkormányzat erőforrásainak zömét felemészti. A költségvetés túlfeszített és kitett a külső hatásoknak, így korlátozottan van forrás szociális vagy közösségi programok megvalósítására. A közösségi közlekedés vonzereje mellett továbbra is jelen van az egyéni gépjárműhasználat. Ha a szolgáltatás versenyképessége csökken, vagy nem tudja követni a város és agglomerációja fejlődését, az ebből fakadó forgalmi hatásokat már nem lehet csak pozitív ösztönzőkkel, érzékeny korlátozások és tiltások nélkül kezelni. Kérdés, hogy a biztonságra törekvő egyének passzív támogatására támaszkodó, felülről irányított rendszer meg tudná-e oldani az ebből fakadó konfliktushelyzeteket.</p>',
  '7a6f9a15-2e71-4bca-a45d-94680f9b4755': '<p>A közlekedési kihívásokra válaszul a város az aktív közlekedés és a “15 perces város” koncepciója mellett köteleződött el, amely 2040-re jelentősen átformálta a köztereket és közlekedési szokásokat. A koncepció lényege, hogy a városlakók alapvető szükségleteit – pl. vásárlás, oktatás, egészségügy, munka – lehetőleg maximum 15 perces sétával vagy kerékpárral el tudják érni. Ez csökkenti az autóforgalmat, javítja a környezet minőségét és a közbiztonságot, valamint élőbbé és egészségesebbé teszi az ennek megfelelően kialakított városi központokat. A közterületi parkolás visszaszorításával több tér nyílik helyi vállalkozásoknak, szabadidős és közösségi tevékenységeknek. Az önkormányzat meglévő európai jó gyakorlatok alapján a vegyes rendeltetésű városrészek kialakítását adókedvezményekkel és közlekedési reformokkal ösztönzi. Az átalakítások hatására pezsgő közösségi élet alakul ki, ahol az emberek aktívan részt vesznek a demokratikus folyamatokban, helyi kezdeményezésekben. </p><br><p>A jövőkép szerint az átalakuló városrészekben élők élvezhetik a zöldebb, egészségesebb környezetet, amely hozzájárul a jobb életminőséghez.  Az átalakulásnak köszönhetően a város vonzóbbá válik, népessége enyhén növekszik. Ez azonban nem egyenlő mértékben csapódik le az egyes városrészekben, és az aktív közlekedés előnyben részesítése sem mindenhol tud érdemi megoldással szolgálni a közlekedési igényekre, emiatt felerősödhet az alacsonyabb jövedelműek kiszorulása, növekedhet a szegregáció. Kérdés, hogy a város fejlődése tud-e kellő erőforrást biztosítani a térbeli különbségek ellentételezésére és csillapítására, illetve az alközpontok közötti közlekedés fejlesztésére úgy, hogy közben folytatja az élhetőséget növelő közterületi átalakításokat.</p>',
  '94b53e83-7875-4c16-9ccf-4becae64f089': '<p>Az elmúlt évtizedek válságaira reagálva a városban a fenntartható életforma vált dominánssá, erős közösségekkel és helyi kezdeményezésekkel. Civil szervezetek, közösségi kertek, sportegyesületek és helyi kulturális programok szervezői formálták át a városi életet és köztereket alulról induló kezdeményezésekkel. Ezzel párhuzamosan a városvezetés fenntarthatóvá tette a közintézményeket és a közösségi közlekedést és támogatta a városlakókat a zöld átállásban. A város fejlődése a gazdasági növekedés, a fogyasztás bővülése és a beruházások ösztönzése helyett minőségi indikátorokban érhető tetten. Elmaradnak a nagyszabású fejlesztések, a város legtöbb része kisvárosias képet mutat, a lélekszám stagnál.</p><br><p>A közlekedési igények mérséklődtek, a saját autók fenntartása drágult, helyettük elterjedtek az elektromos és megosztott járművek, valamint az igényalapú közösségi közlekedés. A köztereken sétáló- és kerékpáros infrastruktúra, zöldfelületek és közösségi terek létesültek. A városlakók számára kiemelten fontos az egészséges környezet, tiszta levegő és alacsony zajszennyezés. Az emberek aktívan részt vesznek a közéletben, erős a közösségi élet és a helyi kezdeményezések folyamatosan dolgoznak a fenntarthatóbb megoldásokon.</p>',
  '1a93946b-27ba-4fd2-a05b-6474b276815c': '<p>2040-re a városi mobilitás jelentős átalakuláson ment keresztül. Széles körben elterjedtek a hagyományos közösségi közlekedés és az egyéni gépjárműhasználat mellett a megosztáson alapuló piaci szolgáltatások, új mikromobilitási eszközök, megjelent az igényalapú közösségi közlekedés és intenzíven fejlődtek a közlekedésszervezés és a parkolás adatalapú, digitális megoldásai is. Online alkalmazásokon keresztül egy felületen, könnyen elérhető és kombinálható szolgáltatásként váltak elérhetővé a különböző közlekedési szolgáltatások. Az önkormányzat a korábban fenntartott hálózatát leépítve teret nyitott ezeknek az új szolgáltatásoknak, hogy vonzóbbá és versenyképesebbé tegye a várost. Nem rendelkezett ugyanakkor elegendő erőforrással a közlekedési szokások befolyásolására: a hatékonyabbá és fenntarthatóbbá váló közlekedési megoldások ellenére az egyéni gépkocsihasználat maradt domináns a város közlekedésében.</p><br><p>A város turizmusra, tudásiparra és kreatívipari beruházásokra összpontosítva felkapott, futurisztikus városi terek jöttek létre, ugyanakkor a közösségi kapcsolatok gyengülnek, növekednek az egyenlőtlenségek és a digitalizáció miatt megritkultak a helyben elérhető szolgáltatások is. A technokrata jövőképben a városlakók alapvetően piaci szolgáltatások fogyasztói, jólétükért és aktív társadalmi részvételükért egyénileg felelősek. A város nem vállalja át a közösség nevében a kockázatokat, csupán egy olyan környezetet biztosít, ahol különböző szolgáltatások szabadon elérhetőek. Ez összességében az egyenlőtlenségek növekedéséhez vezet, miközben gazdasági fellendülések és visszaesések gyakorta váltják egymást.</p>',
  'df6eee27-f75d-430b-bc22-dc3cafa2bc90': '<p>2040-ig a városban folyamatosan és érdemi ellenállás nélkül növekedett a forgalomba álló autók száma, ami egy autóközpontú város- és közlekedéspolitikát rögzített. A legtöbb háztartás legalább két autót tart, mivel a vásárláshoz, gyerekneveléshez vagy a városi környezetből való kiszakadáshoz elengedhetetlen az autó használata. A kerékpárt és az alacsony szintű szolgáltatást biztosító városi buszokat főként a kevésbé tehetős rétegek használják. A városi terek az autóforgalom kiszolgálására vannak kialakítva, gyakoriak a dugók és a forgalom nagy terhet ró az ott lakókra. Sokan költöznek agglomerációs településekre és ingáznak onnan a városba. </p><br><p>Az autóhasználat sokak szemében elkerülhetetlen eleme a városi létnek, ami az ellentmondások ellenére is vonzóbb és kényelmesebb, mint annak alternatívái. A városvezetés forgalmat kiszolgáló infrastruktúra-fejlesztései és a város lakóinak megtartása érdekében magas színvonalon biztosított humánszolgáltatások mellett nincs elegendő forrás a közösségi közlekedés javítására vagy a közterek élhetőbbé tételére. A közlekedés költségei a havi nettó jövedelem jelentős részét elérik, az életszínvonal stagnál. Az emberek többsége azonban elfogadja, hogy önállóan, saját gépjárművet használva, költségesen oldja meg saját közlekedését. Tartanak attól, hogy a közösségi célokért (biztonságosabb közlekedés, tisztább levegő) olyan kényelmetlenségeket kellene elszenvedniük, amellyel egyénileg sokkal rosszabb helyezetbe kerülnének.</p>',
  '1ad707e9-a9c8-4e92-a244-00e156ad25a2': '<p>A város ipari beruházások és ingatlanbefektetések bevonzásával gyors ütemű gazdasági növekedést ért el. Az ehhez szükséges infrastruktúra fejlesztése és a befektetői igények kielégítése azonban jelentős terhet rótt a város költségvetésére. Más területekre, mint a közösségi közlekedés vagy a közterek fejlesztése, nem maradtak erőforrások, a gazdasági szereplők pedig csak korlátozottan vonhatóak be ezek finanszírozásába. Az egyének többségének jólétet biztosító gazdasági fellendülés mellett a város népessége stagnál, folytatódott a kiáramlás az agglomerációba és megnőtt az átmenőforgalom. </p><br><p>A város fejlődése negyedenként jelentős különbségeket mutat, a fejlődésből és a közlekedés terheiből egyenlőtlenül részesülnek az egyes szomszédságok. Mivel a város nem törekszik a hátrányos helyzetű csoportok ellentételezésére, a szegregáció erősödik. Gyakorivá váltak a zárt, őrzött lakóparkok, a magáncégek által fenntartott, nagy területű szolgáltató központok. A belváros a turisták igényei szerint alakult át. Egyes helyeken élhetőbb forgalomcsillapított lakóövezetek jönnek létre, máshol az autóforgalom kiszolgálása alakítja a köztereket. A széttartó fejlődés és a szigetszerű beruházások miatt az egyéni autóhasználat a jellemző közlekedési mód. A város szabályzóként és a versenyképes közösségi közlekedés biztosításában is gyengének bizonyul, nem képes átfogó stratégiát érvényesíteni a város fejlesztésében és a közlekedés ellentmondásainak kezelésében. Az új munkahelyek biztosította viszonylagos jólétben sokan találnak egyéni megoldásokat az egészségtelen környezet nehézségeire, mások azonban úgy látják,  városvezetés csak a munkaerőpiacon aktív, jómódú, fogyasztóképes emberekkel törődik, a szegények, idősek, fogyatékkal élők nem kapnak elegendő figyelmet.</p>',
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
const candidateText = candidatesText[candidateKey] || '';

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
      <BodyText size="medium">
        <div v-html="candidateText" />
      </BodyText>
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
