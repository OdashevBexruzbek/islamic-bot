from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Umumiy buttonlar
main_btn = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="🕋Ислом дини🕋"),
         KeyboardButton(text="🕋Қуръон🕋")],
        [KeyboardButton(text="🕋Намоз🤲"),
         KeyboardButton(text="Рўза")],
        [KeyboardButton(text="🕋Аллоҳнинг муборак исмлар🕋")],
        [KeyboardButton(text="🔖Диний манбалар🔖")],
        [KeyboardButton(text="ШАЙХ МУҲАММАД СОДИҚ МУҲАММАД ЮСУФ")],
        [KeyboardButton(text="🎬Исломий кинолар🎬")],
        [KeyboardButton(text="🎧 Нашидалар 🎧")],
        [KeyboardButton(text="🌐Бот ҳақида🌐")]
    ]
)

#nashidalar
nashidalar = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Тўлин ой порлади - Муҳаммад Аюб қори")],
        [KeyboardButton(text="Расулуллоҳга соғинч нашидаси - Муҳаммад Аюб қори ва Жаннат булбуллариʼ гуруҳи")],
        [KeyboardButton(text="Рамазон нашидаси - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи")],
        [KeyboardButton(text="Қуръоним - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи")],
        [KeyboardButton(text="Оламга нур Пайғамбар - Муҳаммад Аюб қори ва ЪЖаннат булбуллариʼ гуруҳи")],
        [KeyboardButton(text="Асмаул Ҳусна (Аллоҳнинг гўзал исмлари) - Ҳасанхон Яҳё Абдулмажид")],
        [KeyboardButton(text="Асосий мену")]
    ]
    )

#Shayx Muhammad Sodiq Muhammad Yusuf hazratlari
shayx_m = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Шайх Муҳаммад Содиқ Муҳаммад Юсуф")],
        [KeyboardButton(text="Таржимаи холлари"),
         KeyboardButton(text="'Олтин силсиласи'")],
        [KeyboardButton(text="Чоп этилган китоблари")],
        [KeyboardButton(text="Шайх Муҳаммад Содиқ Муҳаммад Юсуф хотирасига эхтиром")],
        [KeyboardButton(text="'Исломга бағишланган умр' ҳужжатли фильм")],
        [KeyboardButton(text="Асосий мену")]
    ]
    )

#Shayx Muhammad Sodiq Muhammad Yusuf hazrat haqida filmlar
hujjatli_film = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="'Исломга бағишланаган умр' траилер")],
        [KeyboardButton(text="'Исломга бағишланаган умр'")],
        [KeyboardButton(text="Xужжатли фильм ҳақида  тарғибот тадбирлари 1-Кисм"),
         KeyboardButton(text="Xужжатли фильм ҳақида  тарғибот тадбирлари 2-Кисм")],
        [KeyboardButton(text="Асосий мену")]
    ]
    )

#Diniy filmlar
islamic_films = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="📽 Муҳаммад Аллоҳнинг элчиси 📽")],
        [KeyboardButton(text="'Дунёнинг яралиши' 1-Кисм"),
         KeyboardButton(text="'Дунёнинг яралиши' 2-кисм")],
        [KeyboardButton(text="📽'РИСОЛАТ' фильми"),
         KeyboardButton(text="📹 Ботмаган Қуёш")],
        [KeyboardButton(text="Имом Ал-Бухорий (узбекфильм) 1998 📽"),
         KeyboardButton(text="📹 Еттинчи бўлинмадаги мўжиза")],
        [KeyboardButton(text="Асосий мену")]
    ]
    )
#maruzalar button
maruzachilar = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Шайх Алижон қори марузалари")],
        [KeyboardButton(text="Асосий мену")]
    ]
    )

#Shayx Alijon qori maruzalari
maruzachi_4 = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="Шайх Алижон қори - Америкадаги ўзбеклар билан суҳбат")],
        [KeyboardButton(text="Шайх Алижон қори - Фарзандга биринчи бўлиб нимани ўргатиш керак?")],
        [KeyboardButton(text="Шайх Алижон қори - Эҳсонга ҳақли бўлганларни ажратиб олинг!")],
        [KeyboardButton(text="Шайх Алижон қори - Қорилар шайхи билан суҳбат.")],
        [KeyboardButton(text="Шайх Алижон қори - Ҳожатингизни фақат ундан сўранг, махлуқидан эмас.")],
        [KeyboardButton(text="Шайх Алижон қори - Беъетибор бўлманг бундай дуо билан дуоингиз ижобат бўлмайди!")],
        [KeyboardButton(text="Шайх Алижон қори - Фотиҳа сурасини ўқиб шифо топганлар")],
        [KeyboardButton(text="Шайх Алижон қори - Аллоҳ азиз қилган зотлар")],
        [KeyboardButton(text="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Бешинчи дарс 1-қисм")],
        [KeyboardButton(text="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Бешинчи дарс 2-қисм")],
        [KeyboardButton(text="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Олтинчи дарс 1-қисм")],
        [KeyboardButton(text="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Олтинчи дарс 2-қисм")],
        [KeyboardButton(text="Шайх Алижон қори - Фотиҳа сурасини шундай ўқингки намозда лаззатланинг")],
        [KeyboardButton(text="Шайх Алижон қори - ҚУРЪОНИ КАРИМ ШАФОАТИ” | 1-ҲАДИС")],
        [KeyboardButton(text="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Еттинчи дарс 1-қисм")],
        [KeyboardButton(text="Шайх Алижон қори - Намозни ҳушу билан ўқиш фазилати. Еттинчи дарс 2-қисм")],
    ]
    )