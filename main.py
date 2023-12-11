from aiogram import Router, Bot, Dispatcher, F, types, html
from aiogram.types import Message, FSInputFile, URLInputFile, InputFile
from aiogram.filters.command import Command
from asyncio import run
from buttons import main_btn, shayx_m, islamic_films, hujjatli_film, nashidalar, maruzachilar, maruzachi_4 #maruzachi_1, maruzachi_2, maruzachi_3,suralar, audio_suralar

tokens = '6503322152:AAEh1BcbAf0TQZNn7ZKcSQM_mw1EKs065Ns'
bot = Bot(token=tokens)

class Musulmon:
    def __init__(self, token=tokens) -> None:
        self.dp = Dispatcher()
        self.bt = Bot(token)

    async def start_message(self, msg: Message):
        name = msg.from_user.full_name
        await msg.answer(f"Ассалому алайкум ва раҳмотуллоҳу ва барокатуҳ. Ҳурматли {name} сиз бу бот орқали ўзингиз учун манфаатли маълумотларни оласиз деб умид қиламан.", reply_markup=main_btn)

    async def main_btn(self, msg:Message):
        post = "Ислом (араб. — бўйсуниш, итоат этиш, ўзини Аллоҳ иродасига топшириш) — жаҳонда кенг тарқалган уч диндан ( буддизм ва христианлик билан бир қаторда) бири. Ислом динига эътиқод қилувчилар арабча ъмуслимʼ(ъсадоқатлиʼ; кўплиги ъмуслимунʼ) деб аталади. Муслимʼ, ъмуслимунъсўзининг бошқа халқлар орасида ўзгача талаффуз этиш (мас, форсларда — мусалмон, ўзбекларда — мусулмон, қирғиз ва қозоқларда — мусурмон, Украина ва Россияда — басурман) натижасида бу динга эътиқод қилувчилар турли ном билан аталади. Лекин буларнинг ичида ҳозир мусулмон ибораси кенг тарқалган. Жаҳонда қарийб 1,7 млрд. киши Исломга эътиқод қилади.Мусулмонларнинг 2/3 қисмидан кўпроғи Осиёдаяшайди. Дунёда мусулмон жамоалари мавжуд бўлган120 дан ортиқ мамлакатдан 40 дан зиёдида мусулмонлараҳолининг кўпчилигини ташкил қилади — Шим. Африка,Ғарбий Осиёнинг барча мамлакатларида ( Кипр, Ливан,Исроил мустасно), Сенегал, Гамбия, Нигер, Сомали,Афғонистон, Покистон, Бангладеш, Индонезия вабошқалар. баъзи мамлакатларда аҳолининг 80% дан ортиғимусулмонлардир. Мусулмонларнинг сони жиҳатдан энг йирикдавлатлар — Индонезия, Ҳиндистон, Покистон ваБангладеш; мусулмонларнинг анчаси Марказий Осиёмамлакатлари, Хитой, Таиланд, Эфиопия, Танзания, Кипрда,Европанинг айрим мамлакатлари.\n\nЯна ҳам кўпроқ маълумотни islom.uz сайтидан олишингиз мумкин."
        if msg.text == '🕋Ислом дини🕋':
            await msg.answer(post)
        
        post2 = "Қуръон (арабча:ўқимоқ, қироат қилмоқ) — мусулмонларнинг асосий муқаддас китоби. Ислом эътиқодига кўра, Қуръон ваҳий орқали Муҳаммад пайғамбарга 610—632 йиллар давомида нозил қилинган Аллоҳнинг каломи (Каломуллоҳ). Қуръон „Китоб“ (ёзув), „Фурқон“ (ҳақ билан ботилнинг орасини айирувчи), „Зикр“ (эслатма), „Танзил“ (нозил қилинган) каби номлар билан аталиб, „Нур“ (ёруғлик), „Ҳудо“ (ҳидоят), „Муборак“ (баракотли), „Мубин“ (очиқ-равшан), „Бушро“ (хушхабар), „Азиз“ (эъзозланувчи), „Мажид“ (улуғ), „Башир“ (башорат берувчи), „Назир“ (огоҳлантирувчи) каби сўзлар билан сифатланган. Ислом оламида Қуръон мусъҳаф номи билан ҳам машҳур. Ислом уламолари Қуръоннинг 30 хил ном ва сифатларини санаб ўтганлар.\n\nЯна ҳам тўлиқ маълумотни islom.uz сайтидан олишингиз мумкин."
        if msg.text == "🕋Қуръон🕋":
            await msg.answer(post2)
        
        if msg.text == "Асосий мену":
            await msg.answer(f"Сиз асосий менуга қайтдингиз.", reply_markup=main_btn)
    
    #namoz_buttons
    async def namoz(self, msg:Message):
        namoz_haqida = "Кишига намоз ўқиш фарз бўлишининг учта шарти бор: Ислом, балоғат, ақл. Лекин етти ёшга тўлган болалар намоз ўқишга буюрилади. Ўн ёшга тўлганида ҳам намоз ўқимаса, ўргатиш мақсадида фақатгина қўл билан урилади, таёқ билан урилмайди. \nИзоҳ: Ҳадиси шарифда Пайғамбаримиз, соллаллоҳу алайҳи ва саллам ЪФарзандларингиз етти ёшга тўлгач, намоз ўқишга буюринглар, ўн ёшга кирганида ҳам намоз ўқимасалар (энгил) уринглар ва ётоқларини ажратингларʼ, деб марҳамат қилганлар.\n\nВожиб бўлишининг сабабиВожиб бўлиш сабаби намоз вақтларининг киришидир. Намознинг аввалги вақти кириши билан бутун вақтнинг бир қисмида уни адо этиш вожибдирИзоҳ: Намоз луғатда дуо деган манони англатади. Шариатда эса бошланиши ифтитоҳ такбири, охири салом бўлган махсус ҳаракат ва лафзлардан иборат ибодатдир. Пайғамбаримизнинг, соллаллоҳу алайҳи ва саллам, ҳижратларидан бир ярим йил аввал, Мерож кечасида фарз қилинган.\n\nМанба ва тўлиқ маълумот: https://islom.ziyouz.com/namoz"
        await msg.answer(namoz_haqida, reply_markup=main_btn)
    
    #ro'za buttons
    async def roza(self, msg:Message):
        roza_haqida = "Рўза, қодир бўлган кишининг ният қилиб, субҳи со-диқдан кун ботгунгача, қасддан ёки янглишиб еб-ичишш дан ва жинсий алоқадан тийилишидир.\n\nРамазон рўзасининг фарз бўлиш сабаби\n\nРўзанинг фарз бўлиш сабаби рўза тутиладиган ойда ё унинг бир қисмида ҳозир бўлишдир. Рамазоннинг ҳар бир куни ўша куннинг рўзасини тутиш фарз бўлишининг сабабидир.\n\nҲукми ва фарз бўлилишнинг шартлари\n\nҚуйидаги учта шарт мавжуд бўлган кишига Рамазоннинг рўзасини вақтида тутиш, агар тута олмаган бўлса, унинг қазосини тутиш фарз бўлади: \n1. Мусулмон, \n2. Ақлли, \n3. Балоғатга етган бўлиши.\n\nРўза тутишиинг вожиб бўлиш шартлари.\n\n1. Рўза тутишга монеъ бўладиган даражада оғир касал бўлмаслик.\n2. Ҳайздан пок бўлиш.\n3. Нифосдан пок бўлиш.\n4. Муқим бўлиш.\nРўза тутишнинг дуруст бўлиш шартлари учта:\n1. Рўза тутишни ният қилиш.\n2. Рўзани бузадиган амаллар қилмаслик.\n3. Ҳайзда, нифосда бўлмаслик.\n\nРукни\nРўзанинг рукни қорин ва жинсий аъзоларнинг истагини ёки буларнинт истаклари ҳукмида бўлган ишларни қилишдан, бажаришдан сақланишдир.\nРўза тутиш натижаси\nФарзни бўйнидан соқит қилиш ва охиратда ажр-савобга эга бўлиш. \n\nМанба ва тўлиқ маълумот:https://islom.ziyouz.com/ruza"
        await msg.answer(roza_haqida, reply_markup=main_btn) 

    #Allohning go'zal ismlari
    async def allohning_ismlari(self, msg:Message):
        malumot = "Аллоҳнинг борлигига ишонган одам У зотни яхши таниши ҳам керак. Ақоид илми истилоҳи билан айтганда маърифат ҳосил қилиши лозим. Бу маърифат эса Аллоҳ таолонинг гўзал исмлари ва У зотнинг сифатларини билиш ила ҳосил бўлади.\nАллоҳ таоло: «Аллоҳнинг гўзал исмлари бордир. Бас, Унга ўша (исм)лар ила дуо қилинг», деган (Аъроф: 180-оят).\nАллоҳнинг барча исмлари гўзалдир. Мўмин-мусулмон банда Аллоҳга дуо қилганида, ўша гўзал исмлар ила дуо қилмоғи лозим.\nАллоҳ таоло яна: «У Аллоҳ Холиқ, Бариъ, Мусаввирдур. Барча гўзал исмлар Уникидир. Осмонлару ердаги барча нарсалар Уни поклаб ёд этадилар. Яна У Азиз ва Ҳакимдир», деган (Ҳашр:24).\n«Ҳашр» сурасининг бу сўнгги оятида Аллоҳнинг бир неча гўзал исмлари ҳақида сўз боряпти. Хусусан:\nХолиқ – яратувчи.\nБариъ – йўқдан бор қилувчи.\nМусаввир – махлуқотларнинг сувратини шакллантирувчи.\nДунёдаги барча чиройли исмлар Аллоҳникидир.\n\nМанба ва тўлиқ маълумот: https://islom.uz/maqola/149"
        await msg.answer(malumot, reply_markup=main_btn)
    async def back_menu(self, msg:Message):
        if msg.text == "Асосий мену":
            await msg.answer("Сиз асосий мену қайтдингиз", reply_markup=main_btn)
        
    #shayx
    async def shayx(self, msg:Message):
        if msg.text == "ШАЙХ МУҲАММАД СОДИҚ МУҲАММАД ЮСУФ":
            await msg.answer(f"Бу бўлим орқали Шайх Муҳаммад Содиқ Муҳаммад  Юсуф хазрат ҳақида маълумотлар оласиз. \n\n    Марҳамат ўзингизга маъқулини танланг.", reply_markup=shayx_m)

    async def shayx_1(self, msg:Message):    
        if msg.text == "Шайх Муҳаммад Содиқ Муҳаммад Юсуф":
            await msg.answer(f"Аллоҳ таоло: «Албатта, Аллоҳдан бандалари ичида фақат олимларгина қўрқарлар», деган (Фотир сураси, 28-оят). \n Расулуллоҳ соллаллоҳу алайҳи васаллам: «Олимлар анбиёларнинг ворисларидир. Анбиёлар динор ҳам, дирҳам ҳам мерос қолдирмаганлар. Улар илмни мерос қолдирганлар. Ким уни олса, улуғ насибани олибди», деганлар (Абу Довуд ва Термизий ривоят қилган). \n Шайх Муҳаммад Содиқ Муҳаммад Юсуф раҳимаҳуллоҳ етук аллома, муфассир, муҳаддис, фақиҳ, муршид, ўз замонасидаги Ислом оламининг йирик намояндаси, улкан арбоб, СССР Олий Кенгашининг халқ депутати, Ўрта Осиё ва Қозоғистон мусулмонлари диний идорасининг собиқ муфтийси, мустақил Ўзбекистоннинг биринчи муфтийси, кўплаб халқаро илмий муассасалар, диний ташкилотларнинг аъзоси, Мовароуннаҳр халқларининг диний раҳнамоси эди. \n Шайх Муҳаммад Содиқ бутун умрини «Аҳли сунна вал жамоа мазҳаби асосида пок ақийда ва мусаффо Исломга интилиш, Қуръон ва Суннатни ўрганиб, амал қилиш, исломий маърифат таратиш, салафи солиҳ – улуғ мужтаҳидларга эргашиш, бағрикенглик ва биродарлик руҳини таратиш, диний саводсизликни тугатиш, ихтилоф ва фирқачиликка барҳам бериш, мутаассиблик ва бидъат-хурофотларни йўқотиш» шиори остида Аллоҳ таолонинг ҳақ динига, У Зотнинг маҳбуб Пайғамбари Муҳаммад мустафо соллаллоҳу алайҳи васаллам келтирган рисолатни тарғиб қилишга бахшида қилиб ўтган саодатманд инсон эди. \n\nМанба: https://islom.uz/hazrat#block1")
    
    async def shayx_2(self, msg:Message):
        if msg.text == "Таржимаи холлари":
            await msg.answer(f"Шайх Муҳаммад Содиқ Муҳаммад Юсуф ҳижрий 1371 йил 21 ражаб, милодий 1952 йил 15 апрель куни Ўзбекистон Республикаси, Андижон вилоятининг Асака туманидаги Ниёзботир қишлоғида, Муҳаммад Юсуф домла хонадонида таваллуд топди. Бошланғич диний таълимни отаси Муҳаммад Юсуф домладан олди. У кишидан асосан тажвид, араб тили грамматикаси – сарф ва наҳв илмларини ўрганди ва Қуръондан бир неча жузларни ёд олди. \n 1969 йили Булоқбоши қишлоғидаги ўрта мактабни тугатиб, 1970 йили Бухородаги Мир Араб мадрасасига ўқишга кирди. \n Собиқ Иттифоқ бўйича у даврдаги ягона диний таълим муассасаси Бухородаги Мир Араб мадрасаси эди. \n\n  Таржимаи холларини тўлиқ ўқиш: https://islom.uz/hazrat#block2")

    async def shayx_3(self, msg:Message):
        if msg.text == "'Олтин силсиласи'":
            await msg.answer(f"«ОЛТИН СИЛСИЛА» ТУРКУМИ ҲАҚИДА \n\nШайх Муҳаммад Содиқнинг сўнгги йиллардаги энг буюк хизматларидан яна бири – «Олтин силсила» деб номланган ҳадислар мажмуасининг академик нашрига бош-қош бўлганидир. «Набавий ҳадисларнинг олтин силсиласи» деб номланган ушбу улкан илмий лойиҳага Ислом оламида эътироф этилган «Кутубу ситта» муаллифлари ҳамда яна уч буюк муҳаддиснинг ҳадислар тўплами киритилди: \n1. «Саҳиҳи Бухорий» \n2. «Саҳиҳи Муслим» \n3. «Сунани Абу Довуд» \n4. «Сунани Термизий» \n5. «Сунани Насоий» \n6. «Сунани Ибн Можа» \n7. «Муваттои Молик» \n8. «Сунани Доримий» \n9. «Саҳиҳи Ибн Ҳиббон» \n   Ушбу улкан академик мажмуа жами 50 жилдга яқин бўлиши кўзда тутилган бўлиб, ушбу муҳаддисларнинг беш нафари буюк алломалар юрти бўлмиш она Ватанимиз, қадим Мовароуннаҳрдан етишиб чиққан муҳаддис имомлар экани ўзбек мусулмонлари учун чинакам фахрдир.\n\n 'Олтин силсиласиʼ туркуми ҳақида тўлиқ маълумот: https://islom.uz/hazrat#block3", reply_markup=shayx_m)

    async def shayx_4(self, msg:Message):
        if msg.text == "Чоп этилган китоблари":
            await msg.answer(f"ЧОП ЭТИЛГАН КИТОБЛАРИ\n\n «Тафсири Ҳилол». Олти жилддан иборат ушбу китоб Қуръони Каримнинг замонавий ўзбек тилида ёзилган биринчи тўлиқ тафсиридир.\n\n • «Қуръони Карим ва ўзбек тилидаги маънолар таржимаси»\n • «Ҳадис ва Ҳаёт» силсиласи. Ал-Азҳар шайхи Мансур Алий Носиф қаламига мансуб «Ат-Тожул жомеъ лил усул фий аҳадисур Расул» номли китобнинг таржимаси ва 37 жуздан иборат шарҳи:\n1. Муқаддима\n2. Ислом ва иймон\n3. Ният, ихлос ва илм\n4. Поклик\n5. Намоз\n6. Намоз\n7. Намоз\n8. Закот\n9. Рўза\n10. Ҳаж\n11. Савдо, зироат ва вақф\n12. Фароиз ва васиятлар\n13. Никоҳ, талоқ ва идда\n14-15. Қасамлар, назрлар ва ов\n16-17. Таом, шароб ва либос\n18. Тиб ва дам\n19. Оламларга раҳмат Пайғамбар\n20. Анбиёлар қиссаси\n\n...Барча китоблар ҳақида қуйидаги ҳавола орқали кўрсангиз бўлади: https://islom.uz/hazrat#block4")

    async def shayx_5(self, msg:Message):
        if msg.text == "Шайх Муҳаммад Содиқ Муҳаммад Юсуф хотирасига эхтиром":
            await msg.answer(f"ШАЙХ МУҲАММАД СОДИҚ МУҲАММАД ЮСУФ ХОТИРАСИГА ЭҲТИРОМ\n\n Президентимиз Шавкат Мирзиёев ташаббуси билан Чилонзор туманида барпо этиладиган масжидга Шайх Муҳаммад Содиқ Муҳаммад Юсуф номи бериладиган бўлди. \nДавлатимиз раҳбари Тошкент шаҳридаги бунёдкорлик ишлари билан танишуви жараёнида мазкур масжид майдонига ташриф буюрди. \nШайх Муҳаммад Содиқ Муҳаммад Юсуф нафақат юртимизда, балки бутун ислом оламида тан олинган олим эди, деди Шавкат Мирзиёев. Ҳаётини муқаддас динимиз арконларини ўрганишга ва тарғиб этишга, халқимиз, ёшларимизни диний маърифат руҳида тарбиялашга бағишлади. \n Дарҳақиқат, Шайх Муҳаммад Содиқ Муҳаммад Юсуф 1989 йилда, жуда қийин ва мураккаб даврда Ўрта Осиё ва Қозоғистон мусулмонлари диний идораси раиси, муфтий бўлди. Бу давр исломий илмлар, диний қадрият ва анъаналар қайта тикланган давр сифатида тарихимизда алоҳида ўрин тутади. \nУ киши ислом оламида маълум ва машҳур бўлган “Мухтасари Виқоя”, “Кифоя”, “Мазҳаблар – бирлик рамзи”, “Мазҳабсизлик – ислом шариатига таҳдид солувчи энг хатарли бидъат” каби китобларни ўзбек тилида шарҳлаб, ўша мураккаб йилларда кўпдан-кўп беҳуда ихтилофларнинг олдини олишга катта ҳисса қўшган. \nМуфтий вазифасида у киши халқаро миқёсда ҳам кенг фаолият юритиб, кўплаб ислом мамлакатлари билан маданий-маърифий алоқаларни йўлга қўйиш ва ривожлантиришга эришган. \nШайх Муҳаммад Содиқ Муҳаммад Юсуф ҳам муфтий, ҳам собиқ Иттифоқ Олий кенгаши депутати сифатида ҳукуматга мусулмонларнинг ҳақ-ҳуқуқларини ҳурмат қилиш, улар учун зарур шароитлар яратиш масалалари кўтарилган махсус баённома тақдим этган. \nМустабид мафкура ҳукмрон бўлган ўша оғир замонда бундай ташаббус билан чиқиш, ҳеч шубҳасиз, катта жасорат эди, деди Президентимиз. Бунинг натижасида шўро ҳукуматининг мусулмонларга нисбатан сиёсати ўзгарган, масжид ва мадрасалар очилган, ҳаж зиёратига борувчилар кўпайган. 1990 йилда Марказий Осиё республикаларидан 500 нафар мусулмон Тошкент шаҳри орқали ҳаж зиёратига боришга муваффақ бўлган эди. Агар ўша даврда бутун собиқ Иттифоқ бўйича ҳар йили бор-йўғи 20-30 киши ҳажга борганини ҳисобга олганда, бу жуда катта натижа бўлган. \nУ кишининг дунё мусулмонлари ўртасидаги обрў-эътибори жуда баланд эди. Бу улуғ ватандошимиз Бутундунё мутафаккир уламолари йиғинининг Ижроия қўмитаси аъзоси, Бутунжаҳон мусулмон уламолари халқаро уюшмаси, Бутундунё Ислом уюшмаси каби нуфузли ташкилотларнинг, Иордания қироллик академиясининг ҳам аъзоси эди. У киши миср Араб Республикасининг “Нил лаври” олтин нишонига сазовор бўлганди. Шуни алоҳида таъкидлаш керакки, замонавий Ўзбекистон тарихида исломий илмлар бўйича ҳеч ким бу даражада юксак мавқега кўтарилмаган. \nБу улуғ аллома турли диний-маърифий мавзуларда 100 дан зиёд китоблар ёзган. Шайх ҳазратларининг ҳикматга тўла сўзлари, суҳбатлари, радио ва телевидение, матбуот саҳифаларидаги доимий чиқишлари, кўплаб китоблари, жумладан, аудиокитоблари орқали юртимиздаги ҳар бир хонадонга кириб борган.\n Шайх Муҳаммад Содиқ Муҳаммад Юсуф ўзининг илми, сўзи ва ибратли амаллари билан она Ватанга, динимиз равнақига чин дилдан ҳалол хизмат қилиш бўйича катта бир мактаб яратиб кетдилар, десак, тўғри бўлади. У кишининг илм ва ҳаёт йўли, бой меросини ўрганиш ва халқимизга етказиш – барчамизнинг бурчимиздир. \n Президентимиз Шавкат Мирзиёев ушбу масжид лойиҳаси билан танишар экан, уни янада такомиллаштириш, бунда халқимиз ва уламоларнинг таклифларини ҳам ўрганиш зарурлигини таъкидлади. \n\nМанба: uza.uz")

    #hujjatli filmalar
    async def shayx_film(self, msg:Message):
        if msg.text == "'Исломга бағишланган умр' ҳужжатли фильм":
            await msg.answer(f"«Исломга бағишланган умр» – шайх Муҳаммад Содиқ Муҳаммад Юсуфнинг ибратли ҳаёт йўли ҳақида фильм.\n  Фильмда шайх Муҳаммад Содиқ Муҳаммад Юсуфнинг болалик йиллари ва таълим олиши, мамлакатни тарк этиши ва қайтиши тарихи, шунингдек, буюк илмий меросига оид маълумотлар акс этган.", reply_markup=hujjatli_film)
    
    async def shayx_film1(self, msg:Message):
        if msg.text == "'Исломга бағишланаган умр' траилер":
            await msg.answer_video(video="BAACAgIAAxkBAAIBoGVDXuKVGx3i2oECJc9UGe7KyMqMAALIIwACNN3RSVv-ffrej-eEMwQ", reply_markup=hujjatli_film)
    
    async def shayx_film2(self, msg:Message):
        if msg.text == "'Исломга бағишланаган умр'":
            await msg.answer_video(video="BAACAgIAAxkBAAIBnmVDXsFO5hrTht9tup5Cueqs_n_GAALgFwAC1TWgSktlh1sbmsQtMwQ", reply_markup=hujjatli_film)
    
    async def shayx_film3(self, msg:Message):
        if msg.text =="Xужжатли фильм ҳақида  тарғибот тадбирлари 1-Кисм":
            await msg.answer_video(video="BAACAgIAAxkBAAIBomVDXv4sjM0t74PZ91WiY9GHWt6RAAKkIAACmaiIS38q738bdWP_MwQ", reply_markup=hujjatli_film)
    
    async def shayx_film4(self, msg:Message):
        if msg.text == "Xужжатли фильм ҳақида  тарғибот тадбирлари 2-Кисм":
            await msg.answer_video(video="BAACAgIAAxkBAAIBpGVDXy67TygxX0R4CuVE7MN6skpiAAIIGAACSVvgSoAQN0zw1R6_MwQ", reply_markup=hujjatli_film)

    #nashidalar
    async def nashidalar(self, msg:Message):
        if msg.text == "🎧 Нашидалар 🎧":
            await msg.answer(f"Сиз нашидалар бўлимидасиз. Марҳамат қуйидаги нашидалардан хоҳлаганизни танлаб тинглашингиз мумкин.", reply_markup=nashidalar)
    
    async def nashid_1(self, msg:Message):
        if msg.text == "Тўлин ой порлади - Муҳаммад Аюб қори":
            await msg.answer_audio(audio="CQACAgIAAxkBAAIDNmVKHyni-tHp8dB3AAEnMRMBwj86zgACMCUAAu_JaEkiVQqTBLdWtDME", caption="Тўлин ой порлади - Муҳаммад Аюб қори")
    
    async def nashid_2(self, msg:Message):
        if msg.text == "Расулуллоҳга соғинч нашидаси - Муҳаммад Аюб қори ва Жаннат булбуллариʼ гуруҳи":
            await msg.answer_audio(audio="CQACAgIAAxkBAAIDO2VKH_RhBiGucStqmLLuyhDQHpuRAAJ8EQACyrWBS177GBLZueSbMwQ", caption="Расулуллоҳга соғинч нашидаси - Муҳаммад Аюб қори ва Жаннат булбуллариʼ гуруҳи")
    
    async def nashid_3(self, msg:Message):
        if msg.text == "Рамазон нашидаси - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи":
            await msg.answer_audio(audio="CQACAgIAAxkBAAIDOGVKH2MTMuZbn7PMqWAXXKsAAf9uzwACuhgAAl3eKUs6oCEPY3rrSjME", caption="Рамазон нашидаси - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи")
    
    async def nashid_4(self, msg:Message):
        if msg.text == "Қуръоним - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи":
            await msg.answer_audio(audio="CQACAgIAAxkBAAIDQGVLGu-R3yppRCq4DAS2l8VP579CAAILGQACr_kZSxSsx2WEAAFJIzME", caption="Қуръоним - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи")
    
    async def nashid_5(self, msg:Message):
        if msg.text == "Оламга нур Пайғамбар - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи":
            await msg.answer_audio(audio="CQACAgIAAxkBAAIDQmVLGwNtAR67eybF6xE-MYU2_cYHAAJFEwACq_qASi3LIQp7ryyMMwQ", caption="Оламга нур Пайғамбар - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи")
    
    async def nashid_6(self, msg:Message):
        if msg.text == "Асмаул Ҳусна (Аллоҳнинг гўзал исмлари) - Ҳасанхон Яҳё Абдулмажид":
            await msg.answer_audio(audio="CQACAgIAAxkBAAIDRGVLGyAeL1MU9FXcV7a6RQ-3nycfAAISEgACpvagSrJuan1wqGgyMwQ", caption="Асмаул Ҳусна (Аллоҳнинг гўзал исмлари) - Ҳасанхон Яҳё Абдулмажид")

    #maruzachilar
    async def maruzachilar(self, msg:Message):
        if msg.text == "Марузалар":
            await msg.answer(f"Quyidagi tugmalardan birini tanlang", reply_markup=maruzachilar) 

    #Shayx Alijon qori maruzalari
    async def maruzachi_4(self, msg:Message):
        if msg.text == "Шайх Алижон қори марузалари":
            await msg.answer(f"Бу бўлимда сиз шайх Алижон қори марузаларини тинглашингиз мумкин. \n\n Марҳамат қуйидаги марузаларидан бирини танлаб тинглашингиз мумкин.", reply_markup=maruzachi_4)
    async def maruzachi_4_1(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Америкадаги ўзбеклар билан суҳбат":
            await msg.answer_video(video="CQACAgIAAxkBAAIDI2VKDyAwan1Kx4VIYImc6Iq6jmexAAIYOAACELSQSCemkYYTmstKMwQ", caption="Шайх Алижон қори - Америкадаги ўзбеклар билан суҳбат")
    async def maruzachi_4_2(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Фарзандга биринчи бўлиб нимани ўргатиш керак?":
            await msg.answer_video(video="CQACAgIAAxkBAAIDJWVKD3-TGPisCfGC10tv6LrcQZxlAALvEwAC_i8BSSkZvCN72etTMwQ", caption="Шайх Алижон қори - Фарзандга биринчи бўлиб нимани ўргатиш керак?")
    async def maruzachi_4_3(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Эҳсонга ҳақли бўлганларни ажратиб олинг!":
            await msg.answer_video(video="CQACAgIAAxkBAAIDJ2VKD5vFLnZVPcK1V_UmYYdUzatiAAI_NQACPb04StC_6mknj98IMwQ", caption="Шайх Алижон қори - Эҳсонга ҳақли бўлганларни ажратиб олинг!")
    async def maruzachi_4_4(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Қорилар шайхи билан суҳбат.":
            await msg.answer_video(video="CQACAgIAAxkBAAIDKWVKD7bXpcZjk1QJbbNhwISAMyKCAAKHOQACx3X5Sc8g9MKYUvkmMwQ", caption="Шайх Алижон қори - Қорилар шайхи билан суҳбат.")
    async def maruzachi_4_5(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Ҳожатингизни фақат ундан сўранг, махлуқидан эмас.":
            await msg.answer_video(video="CQACAgIAAxkBAAIDzWVLMOzCDtV4pjhi-HZFMDMbeFSzAAJwMAACZPfxSEcLTT5oH9CkMwQ", caption="Шайх Алижон қори - Ҳожатингизни фақат ундан сўранг, махлуқидан эмас.")
    async def maruzachi_4_6(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Беъетибор бўлманг бундай дуо билан дуоингиз ижобат бўлмайди!":
            await msg.answer_video(video="CQACAgIAAxkBAAIDy2VLMNmrrETPFYVnuAkslYUqioV7AAIxMAACdV7wSLy5TG2jqhbgMwQ", caption="Шайх Алижон қори - Беъетибор бўлманг бундай дуо билан дуоингиз ижобат бўлмайди!")
    async def maruzachi_4_7(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Фотиҳа сурасини ўқиб шифо топганлар":
            await msg.answer_video(video="CQACAgIAAxkBAAIDyWVLMMOB4MsgYb3VzTomb6o59P-xAAJONQACPb04Svpz-zujA0pKMwQ", caption="Шайх Алижон қори - Фотиҳа сурасини ўқиб шифо топганлар")
    async def maruzachi_4_8(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Аллоҳ азиз қилган зотлар":
            await msg.answer_video(video="CQACAgIAAxkBAAIDx2VLMK6wUvHi4IwMgnOMA70afzo-AAJONgACvqnAS_15sI-q8-N4MwQ", caption="Шайх Алижон қори - Аллоҳ азиз қилган зотлар")
    async def maruzachi_4_9(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Бешинчи дарс 1-қисм":
            await msg.answer_video(video="CQACAgIAAxkBAAIDtmVLLmDr1ZBcaEuBZHuOgDIqXPwgAAKOOAAC1OApStKXPRe9V_kLMwQ", caption="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Бешинчи дарс 1-қисм")
    async def maruzachi_4_10(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Бешинчи дарс 2-қисм":
            await msg.answer_video(video="CQACAgIAAxkBAAIDuGVLLqfaUNvdge6I-72a08reySeBAAISLQACWbhASpmTOf_pFRyeMwQ", caption="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Бешинчи дарс 2-қисм")
    async def maruzachi_4_11(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Олтинчи дарс 1-қисм":
            await msg.answer_video(video="CQACAgIAAxkBAAIDumVLLsdMWmsPyZoJDK6pAT8vo9q6AAJwNQACPb04SnxvzaeRGMd6MwQ", caption="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Олтинчи дарс 1-қисм")
    async def maruzachi_4_12(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Олтинчи дарс 2-қисм":
            await msg.answer_video(video="CQACAgIAAxkBAAIDvmVLLvnFvSxWHTLLydhH41zYNjRLAAJiNQACPb04StYau-ezw_BXMwQ", caption="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Олтинчи дарс 2-қисм")
    async def maruzachi_4_13(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Фотиҳа сурасини шундай ўқингки намозда лаззатланинг":
            await msg.answer_video(video="CQACAgIAAxkBAAIDvGVLLt5xmdROdSsnEcZpIogzmbG2AAKFNAACsFm4Sv_Sv89ZQbfKMwQ", caption="Шайх Алижон қори - Фотиҳа сурасини шундай ўқингки намозда лаззатланинг")
    async def maruzachi_4_14(self, msg:Message):
        if msg.text == "Шайх Алижон қори - ҚУРЪОНИ КАРИМ ШАФОАТИ” | 1-ҲАДИС":
            await msg.answer_video(video="CQACAgIAAxkBAAIDwGVLLxT5mK8yy9bwzfvL7d79DQgDAAJfNQACPb04SpeNRJkoo79_MwQ", caption="Шайх Алижон қори - ҚУРЪОНИ КАРИМ ШАФОАТИ” | 1-ҲАДИС")
    async def maruzachi_4_15(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Еттинчи дарс 1-қисм":
            await msg.answer_video(video="CQACAgIAAxkBAAIDwmVLLyf6LruWo3M5NfBEWcarudZ8AALNOwACa8O4S8W-vDAAAW1qrzME", caption="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Еттинчи дарс 1-қисм")
    async def maruzachi_4_16(self, msg:Message):
        if msg.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Еттинчи дарс 2-қисм":
            await msg.answer_video(video="CQACAgIAAxkBAAIDtGVLLiqz_fKc-BONTsJZ37F7TV6BAAI1PQACBOJZSozDc373Q0xcMwQ", caption="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Еттинчи дарс 2-қисм")
    
    #diniy manbalar
    async def diniy_manba(self, msg:Message):
        text_m = "Ўзбекистон Мусулмолар Идоараси томонидан тасдиқланган расмий веб-саҳифаларни пастдаги ҳаволи орқали кўришингиз мумкин.\n http://old.muslim.uz/index.php/rukn/hamroklar"
        await msg.answer(text_m, reply_markup=main_btn)
   
    async def about_bot(self, msg:Message):
        if msg.text == "🌐Бот ҳақида🌐":
            await msg.answer(f"Бу бот орқали сизга ислом дини ҳақида маълумотлар ва Шайх Муҳаммад Содиқ Муҳаммад Юсуф ҳазратлари ҳақида маълумотлар бериш ҳаракат қилдим, бу маълумотлар сиз учун манфаатли бўлди деб умид қиламан. Ботда барча маълумотлар ислом.уз сайтидан олинди! Келажакда яна ҳам кўпроқ маълумот жойлайман иншааллоҳ.\n\n  Камчиликлари бўлса биздан, яхши бўлган бўлса Аллоҳдан. Фойда топсангиз намозларингизда дуоингиздан умиддамиз! Аллоҳ барчамиздан рози бўлсин 🤲!\n\nБот ҳақида фикр ва таклифларингиз бўлса: @tme_admins га ёзишингиз мумкин.")

    async def islomiy_films(self, msg:Message):
        if msg.text == "🎬Исломий кинолар🎬":
            await msg.answer(f"Бу бўлим орқали исломий кинолар кўришингиз мумкин. Қуйидаги фильмлардан бирини танлаб томоша қилишингиз мумкин.", reply_markup=islamic_films)

    async def film_1(self, msg:Message):
        if msg.text == "📽 Муҳаммад Аллоҳнинг элчиси 📽":
            await msg.answer_video(video="BAACAgIAAxkBAAMyZUHg5EBLFo3iAWSu0EyzAoZOoD8AAmQXAALqWYlLhgJ7C-vaOOwzBA", caption="🌙🕌 Дин ишлари қўмитаси томонидан рухсат берилган — «Муҳаммад (соллаллоҳу алайҳи ва саллам) Аллоҳнинг элчиси» номли фильмнинг ўзбек тилидаги таржимаси эълон қилинди 🤲")
    async def film_2(self, msg:Message):
        if msg.text == "'Дунёнинг яралиши' 1-Кисм":
            await msg.answer_video(video="BAACAgIAAxkBAAM0ZUHg_jHRLVTrqlYiWOZMM9xs6tUAAtsMAAL7z1BJvHSPhFSQkn0zBA", caption="'Дунёнинг яралиши' 1-Кисм")
    async def film_2_1(self, msg:Message):
        if msg.text == "'Дунёнинг яралиши' 2-кисм":
            await msg.answer_video(video="BAACAgIAAxkBAAM2ZUHhGIeWwwHkPBNvAdsN2KFYX18AAvsFAALd93BIUI3NrxiQ8OkzBA", caption="'Дунёнинг яралиши' 2-Кисм")
    async def film_3(self, msg:Message):
        if msg.text == "📽'РИСОЛАТ' фильми":
            await msg.answer_video(video="BAACAgIAAxkBAAM4ZUHhMFlxK7X9XKmSb33Wzu4SShUAAhkEAAILquFIuLUsfSKu3-EzBA", caption="Фильм \n📽'РИСОЛАТ' фильми \n\nСаодат асрига саёҳат қилинг! \n\n•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•\n\nЮқоридаги гўзал ҳикоядан сўнг, Рисолат фильмини сизларга тақдим этмасликдан ҳаё қилдик .  Балким орамиздан яна кимгадир шундай гўзал муҳаббат насиб этар иншаАллоҳ...")
    async def film_4(self, msg:Message):
        if msg.text == "📹 Ботмаган Қуёш":
            await msg.answer_video(video="BAACAgIAAxkBAAM6ZUHhT7e8jxM4lm9l1LgWLssjVWIAAggbAALL6xBLQkqWMCwYmM0zBA", caption="•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•\n📹 Ботмаган Қуёш\n•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•\nФойда топсангиз дуоингиз умидидамиз")
    async def film_5(self, msg:Message):
        if msg.text == "Имом Ал-Бухорий (узбекфильм) 1998 📽":
            await msg.answer_video(video="BAACAgIAAxkBAAM8ZUHhaCScecWeemaVZCLP7kevQTsAAiAFAAJD41lLEoVGlTEX9IYzBA", caption="Имом Ал-Бухорий (узбекфильм) 1998 \n\nФойда топсангиз дуоингиз умидидамиз")
    async def film_6(self, msg:Message):
        if msg.text == "📹 Еттинчи бўлинмадаги мўжиза":
            await msg.answer_video(video="BAACAgIAAxkBAAM-ZUHhfCuQTCq5ZmpkfRMulkf0K78AArMJAALleSFImbTy9MlqLLwzBA", caption="📹 Еттинчи бўлинмадаги мўжиза\n\n•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•\n\n1983 йилда Эгей денгизида бир қизча вафот этади. Вафот этган қизнинг отаси ҳарбий қўмондон бўлиб, айб ақли заиф Мемони бўйнига тушади. Мемо шу денгиз бўйида бувиси ва 7 ёшли қизи билан фақирона ҳаёт кечирарди. Ўлимга маҳкум этилган Мемонинг яқинлари адолат учун курашаётган бир пайтда Мемо ва унинг қизи Ованинг ягона истаги – бирга бўлиш эди. Мемо бу ўлимдан қутулиш учун бир мужиза содир бўлиши керак эди….\n\n•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•\n\nФойда топсангиз дуоингиз умидидамиз")

    async def add_audio(self, msg:Message):
        await msg.answer_audio(audio=f'{msg.audio.file_id}')
        print(msg.audio.file_id)

    def register(self):
        self.dp.message.register(self.start_message,
                             Command(commands="start"))
        self.dp.message.register(self.add_audio, F.content_type == "audio")
        # self.dp.message.register(self.suralars, F.text=="Suralar")
        self.dp.message.register(self.main_btn, F.text == "🕋Ислом дини🕋")
        self.dp.message.register(self.main_btn, F.text == "🕋Қуръон🕋")
        self.dp.message.register(self.back_menu, F.text == "Асосий мену")
        # self.dp.message.register(self.audio_shaklda, F.text=="Audio shaklda")
        # self.dp.message.register(self.audio_suralar, F.text=="Audio suralar")
        self.dp.message.register(self.namoz, F.text == "🕋Намоз🤲")
        self.dp.message.register(self.roza, F.text == "Рўза")
        self.dp.message.register(self.allohning_ismlari, F.text == "🕋Аллоҳнинг муборак исмлар🕋")
        self.dp.message.register(self.diniy_manba, F.text == "🔖Диний манбалар🔖")
        self.dp.message.register(self.shayx, F.text == "ШАЙХ МУҲАММАД СОДИҚ МУҲАММАД ЮСУФ")
        self.dp.message.register(self.shayx_1, F.text == "Шайх Муҳаммад Содиқ Муҳаммад Юсуф")
        self.dp.message.register(self.shayx_2, F.text == "Таржимаи холлари")
        self.dp.message.register(self.shayx_3, F.text == "'Олтин силсиласи'")
        self.dp.message.register(self.shayx_4, F.text == "Чоп этилган китоблари")
        self.dp.message.register(self.shayx_5, F.text == "Шайх Муҳаммад Содиқ Муҳаммад Юсуф хотирасига эхтиром")
        self.dp.message.register(self.islomiy_films, F.text == "🎬Исломий кинолар🎬")
        self.dp.message.register(self.film_1, F.text == "📽 Муҳаммад Аллоҳнинг элчиси 📽")
        self.dp.message.register(self.film_2, F.text == "'Дунёнинг яралиши' 1-Кисм")
        self.dp.message.register(self.film_2_1, F.text == "'Дунёнинг яралиши' 2-кисм")
        self.dp.message.register(self.film_3, F.text == "📽'РИСОЛАТ' фильми")
        self.dp.message.register(self.film_4, F.text == "📹 Ботмаган Қуёш")
        self.dp.message.register(self.film_5, F.text == "Имом Ал-Бухорий (узбекфильм) 1998 📽")
        self.dp.message.register(self.film_6, F.text == "📹 Еттинчи бўлинмадаги мўжиза")
        self.dp.message.register(self.about_bot, F.text == "🌐Бот ҳақида🌐")
        self.dp.message.register(self.shayx_film, F.text == "'Исломга бағишланган умр' ҳужжатли фильм")
        self.dp.message.register(self.shayx_film1, F.text == "'Исломга бағишланаган умр' траилер")
        self.dp.message.register(self.shayx_film2, F.text == "'Исломга бағишланаган умр'")
        self.dp.message.register(self.shayx_film3, F.text == "Xужжатли фильм ҳақида  тарғибот тадбирлари 1-Кисм")
        self.dp.message.register(self.shayx_film4, F.text == "Xужжатли фильм ҳақида  тарғибот тадбирлари 2-Кисм")
        # self.dp.message.register(self.maruzachilar, F.text == "Марузалар")
        self.dp.message.register(self.nashidalar, F.text == "🎧 Нашидалар 🎧")
        self.dp.message.register(self.nashid_1, F.text == "Тўлин ой порлади - Муҳаммад Аюб қори")
        self.dp.message.register(self.nashid_2, F.text == "Расулуллоҳга соғинч нашидаси - Муҳаммад Аюб қори ва Жаннат булбуллариʼ гуруҳи")
        self.dp.message.register(self.nashid_3, F.text == "Рамазон нашидаси - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи")
        self.dp.message.register(self.nashid_4, F.text == "Қуръоним - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи")
        self.dp.message.register(self.nashid_5, F.text == "Оламга нур Пайғамбар - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи")
        self.dp.message.register(self.nashid_6, F.text == "Асмаул Ҳусна (Аллоҳнинг гўзал исмлари) - Ҳасанхон Яҳё Абдулмажид")
        self.dp.message.register(self.maruzachilar, F.text == "Марузалар")
        self.dp.message.register(self.maruzachi_4, F.text == "Шайх Алижон қори марузалари")
        self.dp.message.register(self.maruzachi_4_1, F.text == "Шайх Алижон қори - Америкадаги ўзбеклар билан суҳбат")
        self.dp.message.register(self.maruzachi_4_2, F.text == "Шайх Алижон қори - Фарзандга биринчи бўлиб нимани ўргатиш керак?")
        self.dp.message.register(self.maruzachi_4_3, F.text == "Шайх Алижон қори - Эҳсонга ҳақли бўлганларни ажратиб олинг!")
        self.dp.message.register(self.maruzachi_4_4, F.text == "Шайх Алижон қори - Қорилар шайхи билан суҳбат.")
        self.dp.message.register(self.maruzachi_4_5, F.text == "Шайх Алижон қори - Ҳожатингизни фақат ундан сўранг, махлуқидан эмас.")
        self.dp.message.register(self.maruzachi_4_6, F.text == "Шайх Алижон қори - Беъетибор бўлманг бундай дуо билан дуоингиз ижобат бўлмайди!")
        self.dp.message.register(self.maruzachi_4_7, F.text == "Шайх Алижон қори - Фотиҳа сурасини ўқиб шифо топганлар")
        self.dp.message.register(self.maruzachi_4_8, F.text == "Шайх Алижон қори - Аллоҳ азиз қилган зотлар")
        self.dp.message.register(self.maruzachi_4_9, F.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Бешинчи дарс 1-қисм")
        self.dp.message.register(self.maruzachi_4_10, F.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Бешинчи дарс 2-қисм")
        self.dp.message.register(self.maruzachi_4_11, F.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Олтинчи дарс 1-қисм")
        self.dp.message.register(self.maruzachi_4_12, F.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Олтинчи дарс 2-қисм")
        self.dp.message.register(self.maruzachi_4_13, F.text == "Шайх Алижон қори - Фотиҳа сурасини шундай ўқингки намозда лаззатланинг")
        self.dp.message.register(self.maruzachi_4_14, F.text == "Шайх Алижон қори - ҚУРЪОНИ КАРИМ ШАФОАТИ” | 1-ҲАДИС")
        self.dp.message.register(self.maruzachi_4_15, F.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Еттинчи дарс 1-қисм")
        self.dp.message.register(self.maruzachi_4_16, F.text == "Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Еттинчи дарс 2-қисм")

    async def start(self):
        self.register()
        try:
            await self.dp.start_polling(self.bt)
        except:
            await self.bt.session.close()

if __name__ == "__main__":
    mn = Musulmon()
    run(mn.start())
