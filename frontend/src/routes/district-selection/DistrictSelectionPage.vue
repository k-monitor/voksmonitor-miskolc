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
  'kozossegi-kozlekedes': { name: "Közösségi közlekedés városa", text: `<p style="text-align:justify;"><span>A 2030-as éveket jellemző lassú de tartós gazdasági növekedés közepette az egymást követő városvezetések igyekeztek a globális kihívásokat mérséklő,&nbsp;<strong>kiszámítható jólétet és biztonságot teremteni&nbsp;</strong>minél többek számára és ebben a városi közlekedés átalakítása központi szerepet kapott. Tudatos stratégia mentén zajló fejlesztések eredményeként a várost és agglomerációját fejlett, sűrű közösségi közlekedési hálózattal kötötték össze, amelyet a lakosság többsége megelégedéssel használ.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span >A hozzáférhető árú bérlet és a szolgáltatás magas színvonala, mint&nbsp;<strong>pozitív ösztönzők</strong> hozzájárultak a városon belül az egyéni autóhasználat és a közterületi parkolás visszaszorulásához, a közúti forgalom káros hatásainak mérséklődéséhez. A 2-3 km-nél hosszabb utakat - legyen szó munkahelyre való eljutásról, vagy a belváros szolgáltatásainak igénybevételéről - gazdagon átszőtt közösségi közlekedési hálózat támogatja. A rövidebb távokat gyalogosan vagy mikromobilitási eszközökkel (pl. roller, kerékpár) biztonságos feltételek mellett tehetik meg az emberek. A főbb közlekedési csomópontoknál gyalogos közlekedésre tervezett lakóövezetek, bevásárlóutcák, szolgáltatásokat tömörítő központok alakultak ki, amelyek busszal vagy villamossal könnyen elérhetőek. A belsőégésű motoros járműveket jelentős részt elektromos járművek váltották fel, de ezek száma összességében csökkent. Nem történt olyan technológiai változás sem, ami gyökeresen megváltoztatta volna azt, ahogyan az emberek közlekednek. A digitalizációval, távmunkával kapcsolatos korábbi elvárások is túlzottnak bizonyultak: az emberek továbbra is igénylik a személyes találkozásokat, a belváros kínálta szolgáltatásokat, a közlekedési igények így nem csökkentek, csupán az utazások áthelyeződtek a közösségi közlekedésre.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span >A közlekedési rendszer igen költséges fejlesztése a városlakók befizetései mellett támaszkodik a helyi cégek befizetéseire, illetve a központi és uniós támogatásokra is, amelyet az állam a számára is jelentkező egészségügyi és gazdasági hasznokat, valamint a közlekedési rendszerek összehangolásából eredő hatékonyság-növekedést felismerve biztosít. Erre szükség is van: a közösségi közlekedés a&nbsp;<strong>város költségvetésének legnagyobb tételét jelenti</strong>, amely magában hordozza a kockázatokat. Jelentős összeget emészt fel, hogy az energiaárakban beálló változásokat vagy a klímaadaptációk költségeit és kockázatait a rendszer átvállaja az egyénektől. Ráadásul folyamatos fejlesztést igényel, hogy legalább bizonyos mértékben lépést tartsanak az egyéni vagy megosztott gépjárműhasználatot vonzóbbá tevő, most csak egy szűk réteg által használt piaci technológiai újításokkal.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span >Ezt a rendszert egy erősen központosító városvezetés és a városi cégek befolyásos menedzsmentje működteti, ami felülről, hosszú távú stratégiák mentén irányítja a várost és esetenként a helyi ellenállásokkal is szembeszegülve (pl. forgalomcsillapított zónák kialakítása, közösségi közlekedés előnyben részesítése). Ez a politika ugyanakkor összhangban van a lakosok többségének<strong> politikailag passzív, biztonságra törekvő attitűdjével</strong>. A lakosok egyénileg kevésbé klímatudatosak és az aktív közlekedést használók száma is alacsony marad: a kerékpáros infrastruktúra fejlődése elmarad a közösségi közlekedés mögött.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span >Az egyének számára a közlekedés csekély közvetlen költséggel jár, az egészséges környezettel -&nbsp;<strong>tiszta levegő, alacsony zajszennyezés, balesetek alacsony száma</strong> - párhuzamosan életszínvonaluk és megtakarításaik is növekedhetnek. A lakosságszám csökkenése leáll, a város és térsége egyre vonzóbb lesz a beköltözők számára is. A város gazdasága több lábon áll: erős a turizmus, jelen vannak a térségi jelentőségű ipari beruházások, oktatási és innovációs központok és folyamatosan bővül a szolgáltatói szektor is. A munkahelyek közösségi közlekedéssel jól megközelíthetőek. A jó közlekedés elérhető, megfizethető lakhatást teremt a külső városrészekben és az egyes agglomerációs településeken. Az egyéni közlekedési igények kiszolgálása mellett viszont kevésbé érvényesül a tudatos városfejlesztés: néhány közlekedési csomópont barnamezős fejlesztése kivételével nem jöttek létre vegyes funkciójú, kompakt alközpontok. A belváros kiemelt jelentőségű marad a szolgáltatások és ügyintézés tekintetében. A városszerte jó minőségű közösségi közlekedés mellett nincs igazán motiváló tényező a funkciók helyváltoztatásához, térbeli csomósodásához, kompaktabb városrészek kialakulásához.</span></p><p>&nbsp;</p><p><span>A közösségi közlekedésen alapuló város összességében&nbsp;<strong>ingatag egyensúlyt valósít meg</strong>. Kevésbé ellenálló a külső hatásoknak, gazdálkodása túlfeszített, kevesebb mód van más (pl. szociális vagy közösségi) programok megvalósítására, egyes társadalmi csoportok vagy városrészek hátrányainak kompenzálására vagy a helyi szereplők szabályozás útján történő befolyásolására. Ráadásul az egyéni gépjárműhasználat is számottevő marad, hiszen erre a közösségi közlekedés közúti infrastruktúrája és az aktív korlátozások hiánya lehetőséget ad. Ez pedig konfliktusokat generál, hiszen a város célja közösségi közlekedéssel összekötött, sétára tervezett részek kialakítás, ahol nincs tere az átmenő forgalomnak és a közterületi parkolásnak. Miközben az alacsony költségek és a jó közlekedés csökkenti a szegregációt és mérsékli az egyenlőtlenségeket, az egybefüggő, forgalomcsillapított övezetek és a turisztikai vagy belvárosi területekről a forgalom átterelődik a nem sétáló, kiszolgáló városrészekbe, utcákba. Ha valamilyen okból az emberek elpártolnak a város biztosította közösségi közlekedéstől, vagy az nem tudja követni a város fejlődését, a forgalom könnyen kezelhetetlenné válik, és konfliktusokkal járó aktív korlátozások bevezetése válik szükségessé a pozitív ösztönzők mellett. A modell ráadásul nem terjeszthető ki korlátlanul az agglomerációra, hiszen fenntartása költséges.</span></p>` },
  '15-perces-varos': { name: "15 perces város", text: `<p style="text-align:justify;"><span>A 2020-as évek végére az autóforgalom növekedése olyan mértékű környezeti és biztonsági kihívások elé állította a várost, ami már aktív lakossági ellenállást váltott ki. Egy új szemléletű városvezetés európai jó gyakorlatok alapján, uniós források felhasználásával egy alapvető fordulatot hajtott végre a közlekedéspolitikában és a közterületek kialakítása tekintetében. Célul azt tűzték ki, hogy a város a legélhetőbb európai városok közé kerüljön. A gazdasági értelemben prosperáló időszak jó alapot kínált a város fejlesztésére, a városi közterek széleskörű átalakítására.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span>Az önkormányzat adókedvezményekkel, beépítési szabályozással, gyalogos és forgalomcsökkentett zónák létrehozásával ösztönözte a&nbsp;<strong>vegyes rendeltetésű városrészek&nbsp;</strong>létrejöttét, ahol 15 perces távolságon belül megtalálható minden, a mindennapi élethez szükséges városi funkció. A városi alközpontokban séta- vagy kerékpártávolságra elérhetőek a kereskedelmi egységek, a szolgáltatások, az ügyintézés és a vendéglátóhelyek, az óvoda, iskola, háziorvos. Ezek kialakításához a városi lakótelepek kézenfekvő terepet kínáltak, itt döntően az elmúlt évtizedekben eltűnt kereskedelmi és szolgáltató funkciók újjáélesztése és a szegregációs folyamatok visszafordítása volt a feladat. Más, kertvárosias részeken új, nem lakófunkciók kialakítása, sűrítése és az autóforgalom visszaszorítása jelentett feladatot.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span >Az utcákról nagyrészt<strong>&nbsp;</strong></span><span ><strong>eltűntek a parkoló autók és az átmenő forgalom</strong>, az iskolákat a gyerekek önállóan is biztonságosan tudják megközelíteni.&nbsp;</span><span >Az átalakítások részeként nagy számban alakultak át és újultak meg a közterek: kellemesebb közösségi terek és új zöldfelületek jöttek létre, kisvállalkozók nyitottak üzleteket, a város így hangulatosabb lett és élhetőbbé vált. A vegyes funkcióknak köszönhetően már a nagybevásárláshoz sem kell feltétlenül elmenni a városszéli bevásárlóközpontokig. A legtöbb olyan dolog, amiért korábban autóba kellett ülni, ma gyalog vagy kerékpárral megjárható. Dinamikus, gyors átállás ment végbe, amely találkozott az érintettek életmódjával és gazdasági lehetőségeivel, erősítve a folyamat sikerét. A távmunka, a négynapos munkahét és az e-kereskedelem egyre elterjedtebbé vált bizonyos ágazatokban, némileg csökkentve a munkahelyre ingázók számát.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span>A létrejövő alközpontokban a közlekedési költségek csökkenésével a lakosságnál több pénz marad, amit másra tudnak fordítani. A város élhetősége miatt vonzóbbá , a hosszas ingázás pedig sokak szemében kellemetlenséggé válik, ezért az agglomerációból egyre többen költöznek vissza a városba. Növekszik az életszínvonal, sokat fogyasztanak az emberek, ráadásul az aktív életmód és az egészséges környezet is javítja a közösség jólétét. Erős a szolgáltató szektor, a lakosság egészségtudatossága és az életminősége pedig fókuszba kerül. Tisztább a levegő, alacsony a zajszennyezés, a közlekedési balesetek száma pedig a nullához közelít. A fejlesztésekkel érintett negyedekben a lakosok&nbsp;<strong>fontosnak tartják, hogy beleszóljanak a környezetüket érintő döntésekbe. Nagy az igény a kulturális és szociális programokra, szabadidős tevékenységekre is.&nbsp;</strong>Az itt élő lakosok bekapcsolódnak a lakókörnyezetük alakításába, tiltakoznak az átmenő forgalom ellen (vagy éppen a parkolóhelyeik védelmében) és részt vesznek a közterek kialakításában, fenntartásában. A közlekedésszervezés konfliktusos téma, ám ez nem vezet rendszerszintű ellentmondásokhoz. Az önkormányzat illetékes részvételi irodája digitális eszközökkel és a szomszédsági szinten folyamatos jelenlétet biztosító részvételi pontok hálózatán keresztül becsatornázza a társadalmi igényeket a tervezésbe. A többség számára a környezetkímélő, aktív közlekedés (pl. a kerékpár használata) fontos identitáselem lett, amivel a jólét megtartásával, a fogyasztás visszafogása nélkül is össze tudják egyeztetni a klímatudatosság szempontját mindennapi igényükkel. Ráadásul a lakókörnyezetük látványos fejlődése, élhetőbbé válása együtt jár annak ingatlanpiaci felértékelődésével, ami további ösztönzést jelent az átalakítások támogatásához.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span>A 15 perces városban az utazások többsége gyalog, kerékpárral vagy mikromobilitási eszközökkel történik. Ha mégis messzebbre kell utazni, az autó dominál, de ott, ahol ez hatékonyan fenntartható az alközpontokat közösségi közlekedés is összeköti, illetve megosztott szolgáltatások, magánfenntartású minibuszok is rendelkezésre állnak. Az alközpontokat a belvárossal összekötő bringasztrádákat is megépítették és aktívan használják. Sokan rendelkeznek elektromos kerékpárral. A parkolási rendszer lényegében a város teljes belterületére kiterjed, a díjak magasak és a hét minden napján fizetni kell őket. Az így kialakult városi közlekedési rendszer bevételt termel és rugalmasan reagál a krízishelyzetekre, hiszen csak a központok közötti, magas hatékonyságú, önmagát fenntartó helyi közlekedést kell működtetni. Az önkormányzat forrásait így a város fejlesztésére, illetve közösségi célokra, a helyben munkát adó kisvállalkozások fejlesztésére fordíthatja. Az aktív közlekedés az életmód részévé vált, a járműipar technológiai újításai pedig társadalmilag hatékonyabbá teszik a közlekedést, de nem változtatnak a mindennapi közlekedési szokásokon.</span></p><p>&nbsp;</p>` },
  'fenntarthato-varos': { name: "Fenntartható város", text: `<p style="text-align:justify;"><span>A 2020-30-as éveket rendkívüli válságok jellemezték. A megélhetés költségei és az energiaárak megemelkedtek, ami sokakat az&nbsp;<strong>addigi életvitelük újragondolására késztetett</strong>. A városban a jólétet, a fogyasztást és a gazdasági fejlődést előtérbe helyező, a válságok előtti életmódhoz visszatérni kívánó megközelítéssel szemben többségbe kerültek azok, akik egy kis léptékű, önkéntesen lokális, fenntartható életforma mellett köteleződtek el és ennek mentén kívánták alakítani a város működését is. A kiszámíthatatlan gazdasági környezet, a klímaváltozás és a romló állami közszolgáltatások közepette erős közösségek formálódtak elsősorban az erőforrások megosztása, a szolidaritás és a kölcsönös segítségnyújtás mentén. Civil szervezetek, óvodai - iskolai szülői közösségek, közösségi kertek, szabadidős és sportegyesületek, szakszervezetek, természetvédők, városvédők, egyházi közösségek, önkéntes szemétszedők, helyi kulturális programok szervezői, önfejlesztő és önsegítő egyesületek, kutyás csoportok, energiaközösségek alakultak. Az átalakulás tehát alulról indult, decentralizált módon terjedtek el az először önkéntes, önszerveződő közösségi kezdeményezések a fenntarthatóbb életmód kereteinek megteremtésére. Miközben a városvezetés a lakók többségének közösségi, fenntartható megoldásokra való igényét érzékelve valósít meg szűkös erőforrásaiból rendszerszintű átalakításokat (megújulók használata, városi közösségi közlekedés zöldítése), a változások motorjai a helyi kisközösségek, amelyek folyamatosan dolgoznak a városi léptéknél kisebb, önálló szomszédsági szintű megoldásokon.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span>A saját tulajdonú gépjárművek fenntartása megdrágult, azt a díjak és adók emelésével, a magas károsanyag-kibocsátású járművek tiltásával visszaszorították. Gyors ütemben terjedtek el az elektromos járművek, a megosztott járművek, a közösségi közlekedésben pedig az igényalapú szolgáltatások. Gyakori, hogy egy autót több család vagy baráti társaság közösen használ. Szinte mindenki aktívan használ mikromobilitási eszközöket vagy kerékpárt. A közterületi parkolás helyett az utcákon sétáló és kerékpáros infrastruktúra, a klímaadaptációt szolgáló zöldfelületek és közösségi terek kaphattak helyet. A városlakók nagy megelégedésére a városon átfolyó patak mentén egy élhető kék-zöld folyosó alakult ki. Kiemelt jelentőségű az egészséges környezet, a tiszta levegő és az alacsony zajszennyezés, a közlekedési és fogyasztási igények ugyanakkor mérséklődtek. Sokan önkéntesen igyekeznek minimalizálni online jelenlétüket. Számos kezdeményezés indult a helyi gazdaság felpörgetésére, alternatív gazdasági modellek bevezetésére, ami egyre több helyi lakosnak ad munkát és megélhetést anélkül, hogy napi szinten ingáznia kellene a munkahelyre.&nbsp;</span></p><p>&nbsp;</p><p style="text-align:justify;"><span>Az agglomerációs kiköltözés leállt, a városban jobbak a lehetőségek a fenntarthatóbb, alacsonyabb költségű, kisebb ökológiai lábnyomú életvitelre. Sokan saját megtakarításaikból is beruháznak a zöld átállásba, ehhez a város kedvező feltételeket kínál. A közösségi élet erős, a legtöbben tagjai valamilyen egyesületnek, csoportnak, gyakran fontos városi funkciók is ilyen közösségek, közösségi intézmények körül csomósodnak. Sokan maguknak termelik meg az élelmiszer egy részét: hódítanak a kiskertek, a termelői piacok és a szövetkezetek. A város zöldebb, rendezett kisvárosi képet mutat: elmaradtak a nagy infrastrukturális és ipari beruházások, nincs nagy különbség a központi és a városszéli részek között. Szennyező ipari beruházásokat már nem engednek letelepedni a városban, és a tömegturizmus visszaszorítását is sokan követelik, ez ugyanakkor sok embernek ad munkát.</span></p><p style="text-align:justify;"><span>Az emberek nyitottak a változtatásokra, hajlandóak nagyobb áldozatot vállalni a mindennapi gyakorlataikban azért, hogy a közösségi szinten optimálisnak és helyesnek gondolt megoldások működhessenek. Aktívan vitatják meg a helyi közügyeket, részt vesznek a közéletben. Vannak azonban kimaradók is: a korábban is meglévő szegregációt a fenntartható életmód körüli törésvonal tovább erősítette. Sokan úgy érzik, kárvallotjai lettek a zöld átmenetnek, ami jelentős költséget hárít rájuk. Ők továbbra is nyitottak egy kevésbé fenntartható, erőteljesebb iparosítást és gazdasági növekedést ösztönző várospolitika iránt.</span></p>` },
  'hi-tech-varos': { name: "Hi-tech város", text: `<p style="text-align:justify;"><span>A 2030-as években a városi mobilitás jelentős változásokon ment keresztül. A hagyományos közösségi közlekedés egyre több mobilitási lehetőséggel kényszerült versenyre. Korábban egy szűk réteg szokásának tűnt, mára azonban kortól függetlenül elterjedt az autó- és kerékpármegosztás, az igény szerinti közlekedés, az okosparkolás és a fuvarmegosztás, illetve a telekocsirendszer. Folyamatosan formálódnak az emberek igényei, piaci szolgáltatások nyernek teret és tűnnek el.&nbsp;<strong>Digitális alkalmazásokkal&nbsp;</strong>egy felületen váltak elérhetővé a különböző közlekedési szolgáltatások: információk, útvonaltervezés, vásárlás, foglalás, akár különböző szolgáltatóktól, változatos pénzügyi konstrukcióban. A városi közösségi közlekedési szolgáltatások ugyanígy elérhetőek itt, mint a magáncégeké. A közlekedési és logisztikai helyzeteket is ezek a felülről irányított, a felhasználók adataihoz szabadon hozzáférő ökoszisztémák igyekeznek - a várossal együttműködve - hatékonyabbá tenni, nehezen átlátható és számonkérhető algoritmusok mentén.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span>Az önkormányzat passzív szereplő volt ebben az átalakulásban. Igyekezett teret biztosítani a felfutóban lévő megoldásoknak, hogy ezzel vonzó, versenyképes városként tűnjön fel és befektetéseket, jómódú, kreatív lakosokat vonzzon be, javítva pozícióját a városok versenyében. Saját közösségi közlekedési szolgáltatásait jelentősen leépítette, és amit megtartott, azt igyekezett fejleszteni, megtérülőbbé és versenyképesebbé tenni a sikeres platformok mintái szerint. A platformokat és piaci megoldásokat alacsony adókkal és rugalmas szabályozásokkal is csábítják a városba. Azonban a városnak se erőforrása, se kapacitása nincsen, hogy érdemben befolyásolja a közlekedési szokásokat vagy segítse a rendszerből kimaradókat. A szabályozások egy lépéssel a piaci folyamatok mögött járnak, lényegében csak akkor avatkoznak be, ha a trendek tarthatatlan helyzeteket generálnak. A tiltások és korlátozások nem bizonyulnak hatékonynak, a platformok megkerülik azokat, máshová helyezve át a forgalmat, így az önkormányzat inkább partnerségre törekszik a szolgáltatókkal. A helyi fenntartású közösségi közlekedés kevés erőforrással működik, ezért csak néhány viszonylaton hatékony a piaci versenytársaihoz és az autóhasználathoz képest. A város polgára fogyasztóvá válik, a közösségi céloknak való alárendelés helyett a közlekedés az ő egyéni igényeit (és a szolgáltató cégek profitigényét) elégíti ki. Az egyének&nbsp;<strong>választásaikért közvetlenül maguk viselnek felelősséget</strong>, a cégek vagy a város nem ígérnek biztonságot, igazságosságot vagy jóllétet, csupán az elérhető leghatékonyabb technológiai megoldásokhoz való hozzáférést.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span>Miközben a technológiai megoldások magasabb kihasználtságot, valamivel hatékonyabb köztérhasználatot és okosabb közszolgáltatásokat tesznek lehetővé (pl. több elektromos, megosztott járművet hoznak be a közlekedésbe). A megosztott szolgáltatások mellett az egyéni gépkocsihasználat marad az alapvető közlekedési mód, különösen azok számára, akik a város agglomerációjában élnek és nem feltétlenül férnek hozzá az új szolgáltatásokhoz. A fenntarthatóság másodlagos kérdés, a fogyasztókat alapvetően a szolgáltatások minősége és költsége érdekli. A város külső forrásokra alapozó, a helyi lakosok igényeit kevésbé figyelembevevő turisztikai, tudásipari és kreatívipari nagyberuházásokra és a piaci befektetések bevonzására összpontosít. Ezeken a zöld és élhető, olykor futurisztikus városi tereken kívül a közterületeken megmaradnak a parkolóhelyek, megjelennek a mobilitási pontok, rakodóhelyek. Összefüggő kerékpáros infrastruktúra nem épül ki. Az ülő életmód és a közlekedés káros hatásai növekvő költséggel járnak mind az egyénnek, mind pedig a közösségnek. A társadalom tehetősebb rétegei sokat költenek egészségre és sportra. A gépkocsik csak a belváros hagyományos sétálóutcáiból és néhány új, zárt lakónegyedből, sétálásra tervezett szolgáltató életmód-központból vannak kiszorítva vagy dinamikus árszabású parkolással korlátozva. Az alapvető városi közszolgáltatások és infrastruktúra alacsony színvonalú, elhanyagolt, a helyét sok esetben magánszolgáltatások veszik át.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span>A város szétterülése folytatódik: új monofunkciós városrészek jönnek létre a szabadon beépíthető területeken, ahol a szolgáltatások és lakófunkciók elkülönülnek egymástól. A kiskereskedelem visszaszorulóban van, terjednek az önkiszolgáló üzletek és éttermek. A belvárosban egyaránt vannak elit fogyasztási terek és a leromlott állapotú (szlömösödő) részek. A mindennapi lét nélkülözhetetlen részévé válik a távmunka, az online kereskedelem és az ételkiszállítás, emiatt - és a kaotikussá váló városszerkeszet miatt - a közlekedési igény nő. Az egyéni fogyasztás és a digitális kapcsolattartás elsődlegessége miatt a közösségi kapcsolatok gyengülnek, a közügyek helyét a fogyasztáshoz kapcsolódó terek és közösségek veszik át. A közlekedésre fordított kiadás a havi nettó jövedelem 20 százalékát is eléri, az életszínvonal stagnál. Növekednek az egyenlőtlenségek, sokan kiszorulnak a városból és nem férnek hozzá a jólétet biztosító szolgáltatásokhoz. Bár a közlekedési rendszer folyamatos változásban van, klímaadaptációja drága és körülményes, a külső sokkok pedig jelentős terheket rónak az egyénekre és a városra. Bár a technológiai fejlesztések időről időre pozitív hatásokat váltanak ki, leginkább a piaci költségeket csökkentik, miközben újabb költségeket terhelnek rá az ehhez alkalmazkodni kénytelen városra és lakóira. Egy esetleges gazdasági válság és a kereslet csökkenése lefelé tartó spirálba lökné a várost, ami sokakat arra késztethet, hogy erős kötődés híján máshol próbáljon szerencsét.</span></p>` },
  'autokozpontu-varos': { name: "Autóközpontú város", text: `<p style="text-align:justify;"><span >A folyamatos forráshiánnyal küzdő városi közösségi közlekedés elveszítette a versenyt az egyéni gépkocsihasználattal szemben. 2040-re a legtöbb utazás autóval történik, a saját autó az egyéni szabadság, kényelem és a teljeskörű társadalmi részvétel garanciája, amiről senki sem akar lemondani. A jogosítványszerzés a nagykorúságot, az önállóságot jelenti. A város büszkesége, hogy a legújabb elektromos modellek akkumulátorai a városban készülnek. Bár egyre elterjedtebbé vált a távmunka és az online vásárlás, a bevezetőutak mellett álló bevásárló- és szolgáltatóközpontok továbbra is népszerűek, az autók száma pedig mégis évről évre növekszik a városban. Nemcsak vásárláshoz, de a városból való kiszakadáshoz és szabadidős tevékenységhez is<strong> elengedhetetlenné vált kocsiba ülni.</strong> A legtöbb háztartás legalább két saját autót tart, különösen ha a munkába járás mellett a gyerekek iskolába szállítását is biztosítani kell. Kerékpárral vagy a sokszor megbízhatatlan városi buszokkal lényegében már csak azok próbálnak közlekedni, akik ezt nem engedhetik meg maguknak. A saját autótól való megfosztottság lényegében a szegénységgel, a bizonytalan munkalehetőséggel egyenlő.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span >A városi terek használatát az autóforgalom kiszolgálása határozza meg, ezen a technológiai újítások (automatizáció, elektromos járművek terjedésének tudatos támogatása) sem változtatnak. A&nbsp;<strong>város igyekszik kiszolgálni a növekvő forgalmat és megküzdeni az anomáliákkal:</strong> döntően elektromos taxik és szállítójárművek közlekednek, a parkolókat bővítik, új elkerülő utak épülnek, a forgalom zavartalansága érdekében a&nbsp;</span><span>közlekedési módok szétválasztására törekednek, igyekezve a mellékutcákból gyűjtőutakra terelni a forgalmat. Ezzel együtt rendszeresek a dugók és a belvárosban, illetve a forgalmas gyűjtőutak környékén a közlekedés alig elviselhető terhet jelent a még ott lakóknak. A közlekedési terhelést elszenvedő kiszolgáló részek kiürülnek, haldokló kiskereskedelem, kevés elérhető szolgáltatás a jellemző, miközben a munkahelyek nagy része is a városszéli ipari parkokban, és kereskedelmi zónákban található. A városon belül<strong> kevés a zöld, sok a burkolt felület, minimális társadalmi érintkezésre van lehetőség a köztereken</strong>. Az autóforgalom csak a belváros néhány hagyományosan sétálóutcaként működő részéről van kitiltva. Felértékelődnek a parkok és a közeli természetes zöldterületek, de így ezeken a részeken is jelentős forgalom jelenik meg és állandó problémát&nbsp; jelent a parkolás.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span>Aki teheti, a csendesebb agglomerációs települések autóval elérhető új lakóparkjaiba vagy kertvárosi övezeteibe költözik és innen&nbsp;<strong>ingázik városi munkahelyére</strong>. A város népessége így folyamatosan csökken, elöregedik. Ezt a tendenciát erősíti az egészségtelen levegő, a zaj és a sok közúti baleset is. A közlekedés költségei a havi nettó jövedelem 25-30%-át elérik az energiaárak növekedése és a zöld átállás érdekében a gépjárművekre kivetett adók miatt, így az életszínvonal - és vele a város gazdasága is - stagnál.</span></p><p style="text-align:justify;"><span >A város nehezen bírkózik meg a folyamatos, részben a forgalom növekedését, részben a helyi ipari parkok befektetőit kielégítő infrastruktúra-beruházások költségeivel. Ehhez adódik, hogy a a feszültségek csillapítása érdekében, kompenzációs jelleggel&nbsp;<strong>magas színvonalú kulturális, egészségügyi és szociális szolgáltatásokat is biztosítanak</strong>, amelyekkel próbálják helyben tartani a családokat és a kritikus fontosságú munkaerőt. Mivel a domináns politikai erők nem állnak elő radikálisan más közlekedési vízióval, inkább a humánszolgáltatások területén versengenek egymással. A kiadások miatt jelentős közterületi átalakításokra, a közösségi közlekedés versenyképesebbé tételére nincs forrás. A társadalmi elvárásokkal szemben kész öngyilkosság lenne a városvezetés részéről, ha draszikus eszközökkel próbálná visszaszorítani vagy bevételszerzés céljából drágítani az autóhasználatot. Így a város vezetői inkább arra törekszenek, hogy a leginkább rászorulók (idősek, gyermeket nevelők, hátrányos helyzetűek) számára biztosítsanak előnyöket a közlekedésben. A parkolási rendszer a legzsúfoltabb részekre és időszakokra összpontosít, és kiterjedt kedvezményeket biztosít a helyi lakosok számára.</span></p><p style="text-align:justify;"><span >Az emberek többsége a mindennapok részének tekinti az autós közlekedéssel járó kellemetlenségeket, és nem igényli a nagyobb beleszólást, vagy a közösségi élet tereinek kibővítését, hiszen alapvetően egyéni megoldásokban gondolkodik. Bár vannak vagyoni különbségek, de a közlekedés tekintetében egy meglehetősen homogén, ha úgy tetszik, egyenlőségelvű (autóközpontú) megközelítés dominál, ami ódzkodik attól, hogy a közterek újrafelosztásával, vagy különbségtélek bevezetésével bármelyik csoportot előnyben vagy hátrányban részesítsen a jelenlegi helyzethez képest. A többség szemében a jelenlegi helyzet egy viszonylag kényelmes egyensúlyt valósít meg, amelynek felborítása feszültségeket generálna és veszélyeztetné a helyi lakosoknak biztosított előjogokat és a környező településeknél magasabb színvonalú közszolgáltatásokat.</span></p>` },
  'regios-gazdasagi-kozpont': { name : "Régiós gazdasági központ", text: `<p style="text-align:justify;"><span>Az elmúlt évtizedek városvezetései a város fejlődésének kulcsát abban látták, hogy befektetőket csábítsanak a városba, bízva abban, hogy a gazdasági növekedés stabil jólétet biztosít a lakosság számára. A város jelentős költséget vállalt az infrastruktúra fejlesztésében: ipari parkok infrastruktúrájának kiépítésében, a külföldi befektetők és menedzserek számára vonzó presztízsberuházások (pl. nemzetközi iskola, repülőtér) fejlesztésében, valamint - bár ezen a téren jelentős hiányosságok tapasztalhatóak -&nbsp; az új ingatlanberuházások infrastruktúrával való ellátásában. Mindez erősen megterhelte a város költségvetését. Más területekre, mint a városi közösségi közlekedés szisztematikus fejlesztésére vagy élhető közterületek kialakítására nem maradtak erőforrások, a város pedig mindinkább sodródni kezdett a gazdasági folyamatokkal, foglyává vált a befektetői érdekeknek.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span >A gazdasági szereplőkkel összefonódó, vállalkozó felfogású önkormányzati vezetés ugyan törekszik arra, hogy egyfelől jobban bevonja a befektetőket az infrastruktúra fejlesztésébe és a közösségi közlekedés finanszírozásába, másfelől, hogy tervszerű lépésekkel avatkozzon be a közlekedési anomáliák megoldása érdekében akár forgalomkorlátozással, a közösségi közlekedés előnyben részesítésével. A folyamatos fejlesztésekkel azonban nem tudja tartani a lépést, az ezek generálta hatások mindig túllépnek rajta. A város a zöldebb, élhetőbb környezetet célzó intézkedéseit csak akkor tudja megvalósítani, ha azok a befektetői érdekekkel is összhangban vannak.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span >Az elővárosokban zajló, iparfejlesztéshez kapcsolódó közúti és vasúti fejlesztések gyakran nem az itt élők számára hasznosultak, sőt növelték az átmenő forgalmat. Folyamatossá vált a városban a nehézgépjárművek jelenléte és megnőtt az ingázók száma. 2040-re az ipari beruházásokkal a város mindennapjainak részévé váltak a vendégmunkások. A városban ugyan gazdasági pezsgés van és folyamatosak a beruházások, a város lakónépessége azonban összességében stagnál. Folytatódik a kiáramlás a városból elővárosi lakóparkok, bevásárlóközpontok építésével. Kezdetben a város igyekezett hatékony, elérhető árú közösségi közlekedést fenntartani, különösen a munkába járás kiszolgálásához, de a növekvő jövedelmek mellett ez fokozatosan versenybe kényszerült az egyéni gépkocsihasználattal. A város ciklikusan fellépő pénzügyi nehézségei a közösségi közlekedést is érintették, így 2040-re már dominánssá vált az egyéni gépjárműhasználat. A közösségi közlekedés már nem tudja megfelelően kiszolgálni a városban szétszórva megjelenő új lakónegyedeket és kereskedelmi-szórakoztató központokat. A város szabályzóként és koordinátori szerepben gyengének bizonyult, nem képes átfogó stratégiát érvényesíteni a város fejlesztésében.&nbsp;</span><span>Egyedi kezdeményezésekre, lobbik hatására történnek a magánberuházások, nem alakulnak ki kompakt negyedek, ez a fragmentáltság pedig még inkább az autóhasználatnak kedvez. Nem feltétlenül illeszkedő közlekedési megoldások alakulnak ki a városban, akár egymástól néhány utcára.</span></p><p>&nbsp;</p><p style="text-align:justify;"><span >A fejlődésből egyenlőtlenül részesülnek az egyes társadalmi csoportok. A szegregáció erősödik, gyakorivá váltak a zárt, őrzött lakóparkok, a magánszolgáltatóknak bérbe adott közterek, privát klubok. A város által fenntartott közösségi közlekedés néhány főbb útvonalra szorult vissza, de vegyes konstrukcióban számos iparvállalat és üzletközpont működtet különjáratokat, olykor egymással párhuzamosan. Egyes viszonylatokban megjelentek az iránytaxik. A biztonságos kerékpáros közlekedés feltételei nem adottak. A köztereket továbbra is a szűk járdák és a parkoló autók dominálják, bár néhány új építésű negyed közelében zöldebb, besétálható területeket is kialakítottak. A belvárosba rengeteg tőke koncentrálódott, de a magas presztízsű üzletek és szolgáltatások itt főképp a turistákra összpontosítanak.</span></p><p style="text-align:justify;"><span>Más negyedekben alig elérhetőek a különböző szolgáltatások, lévén a keresletet a plázák elszívják. Bár a város gazdasági értelemben prosperál, a jövedelem 20-30 százalékát is felemészthetik a közlekedéshez kapcsolódó kiadások. A kritikusok szerint a városvezetés csak a munkaerőpiacon aktív, jómódú, fogyasztóképes emberekkel törődik, a szegények, idősek, fogyatékkal élők nem kapnak elegendő figyelmet. Egyre többeket zavar az egészségtelen környezet, a magas zaj- és légszennyezés, a közúti balesetek és halálozások magas száma, de a város közéletében megkerülhetetlen a gazdasági fejlődést előtérbe helyező érdekcsoport, ami nem kívánja jobban bevonni a vállalatokat a helyi közügyek megoldásába.</span></p>` },
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
          <SecondaryNavigationBar transparent centered-title>
            <TitleText tag="h2" size="medium">{{ title }}</TitleText>
          </SecondaryNavigationBar>
      </template>
        <BottomBarWrapper>
          <div class="main">
            <img :src="'/data/instance/voksmonitor.hu/parkolasi-jovokepek/voksmonitor/images/candidates/'+electionStore.selectedElectionKey+'.webp'" width="100%">
            <BodyText tag="p" size="medium">
              <div v-html="text" />
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
  background: rgb(248, 247, 247);
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
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
}

/* TODO: update breakpoint */
@media (max-width: 700px) {
  .main {
    grid-template-columns: 1fr;
  }
}

img {
  margin-bottom: 10px;
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
