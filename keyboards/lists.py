"""модуль списков для кнопок и подсказок"""
commands_list = [
    '/anime_search', '/manga_search', '/search_characters',
    '/search_img_anime', '/my_collecion'
]
preview_text="list of commands: \n" \
             "/anime_search: i'll help you find anime\n" \
             "/manga_search: if you need to find manga\n" \
             "/photo_search: find an anime by picture\n" \
             "/char_search: searching for a character\n" \
             "/collections_anime: your anime collections\n" \
             "/collections_manga: your manga collections\n" \
             "/favourite_characters: your favourite characters"
list_of_collections = {
    "favorite": f"\U00002B50",
    "planned": f"I'll see",
    "in_process": f"in the process",
    "finished": f"Viewed"
}
media_search_options = ['name', 'genres', 'rank', 'tags', '\U0001F50E']
media_rank = [i for i in range(1, 10)]
media_genre = [
    'action', 'adventure', 'comedy', 'drama', 'ecchi', 'fantazy', 'horror',
    'mahou shoujo', 'mecha', 'music', 'mystery', 'psychological', 'romance',
    'sci-fi', 'slice of life', 'sports', 'supernatural', 'thriller'
]
tag_list = [
    '4-koma', 'achromatic', 'achronological order', 'acting', 'adoption',
    'advertisement', 'afterlife', 'age gap', 'age regression', 'agender',
    'agriculture', 'ahegao', 'airsoft', 'alchemy', 'aliens',
    'alternate universe', 'american football', 'amnesia', 'amputation',
    'anachronism', 'anal sex', 'angels', 'animals', 'anthology',
    'anthropomorphism', 'anti-hero', 'archery', 'armpits',
    'artificial intelligence', 'asexual', 'ashikoki', 'asphyxiation',
    'assassins', 'astronomy', 'athletics', 'augmented reality',
    'autobiographical', 'aviation', 'badminton', 'band', 'bar', 'baseball',
    'basketball', 'battle royale', 'biographical', 'bisexual', 'blackmail',
    'body horror', 'body swapping', 'bondage', 'boobjob', 'boxing',
    "boys' love", 'bullying', 'butler', 'calligraphy', 'cannibalism',
    'card battle', 'cars', 'centaur', 'cgi', 'cheerleading', 'chibi',
    'chimera', 'chuunibyou', 'circus', 'classic literature', 'clone',
    'college', 'coming of age', 'conspiracy', 'cosmic horror', 'cosplay',
    'crime', 'crossdressing', 'crossover', 'cult', 'cultivation', 'cumflation',
    'cunnilingus', 'cute boys doing cute things',
    'cute girls doing cute things', 'cyberpunk', 'cyborg', 'cycling',
    'dancing', 'death game', 'deepthroat', 'defloration', 'delinquents',
    'demons', 'denpa', 'detective', 'dilf', 'dinosaurs', 'disability',
    'dissociative identities', 'dragons', 'drawing', 'drugs', 'dullahan',
    'dungeon', 'dystopian', 'e-sports', 'economics', 'educational', 'elf',
    'ensemble cast', 'environmental', 'episodic', 'ero guro', 'espionage',
    'exhibitionism', 'facial', 'fairy tale', 'family life', 'fashion', 'feet',
    'fellatio', 'female harem', 'female protagonist', 'femdom', 'fencing',
    'firefighters', 'fishing', 'fitness', 'flash', 'flat chest', 'food',
    'football', 'foreign', 'found family', 'fugitive', 'full cgi',
    'full color', 'futanari', 'gambling', 'gangs', 'gender bending', 'ghost',
    'go', 'goblin', 'gods', 'golf', 'gore', 'group sex', 'guns', 'gyaru',
    'handball', 'handjob', 'henshin', 'heterosexual', 'hikikomori',
    'historical', 'homeless', 'human pet', 'hypersexuality', 'ice skating',
    'idol', 'incest', 'inseki', 'irrumatio', 'isekai', 'iyashikei', 'josei',
    'judo', 'kaiju', 'karuta', 'kemonomimi', 'kids', 'kuudere', 'lacrosse',
    'lactation', 'language barrier', 'large breasts', 'lgbtq+ themes',
    'lost civilization', 'love triangle', 'mafia', 'magic', 'mahjong', 'maids',
    'makeup', 'male harem', 'male protagonist', 'martial arts', 'masochism',
    'masturbation', 'medicine', 'memory manipulation', 'mermaid', 'meta',
    'milf', 'military', 'mixed gender harem', 'monster boy', 'monster girl',
    'mopeds', 'motorcycles', 'musical', 'mythology', 'nakadashi', 'necromancy',
    'nekomimi', 'netorare', 'netorase', 'netori', 'ninja', 'no dialogue',
    'noir', 'non-fiction', 'nudity', 'nun', 'office lady', 'oiran',
    'ojou-sama', 'omegaverse', 'orphan', 'otaku culture', 'outdoor',
    'pandemic', 'parkour', 'parody', 'philosophy', 'photography', 'pirates',
    'poker', 'police', 'politics', 'post-apocalyptic', 'pov', 'pregnant',
    'primarily adult cast', 'primarily child cast', 'primarily female cast',
    'primarily male cast', 'primarily teen cast', 'prostitution', 'public sex',
    'puppetry', 'rakugo', 'rape', 'real robot', 'rehabilitation',
    'reincarnation', 'religion', 'revenge', 'rimjob', 'robots', 'rotoscoping',
    'rugby', 'rural', 'sadism', 'samurai', 'satire', 'scat', 'school',
    'school club', 'scissoring', 'scuba diving', 'seinen', 'sex toys',
    'shapeshifting', 'ships', 'shogi', 'shoujo', 'shounen', 'shrine maiden',
    'skateboarding', 'skeleton', 'slapstick', 'slavery',
    'software development', 'space', 'space opera', 'spearplay', 'squirting',
    'steampunk', 'stop motion', 'succubus', 'suicide', 'sumata', 'sumo',
    'super power', 'super robot', 'superhero', 'surfing', 'surreal comedy',
    'survival', 'sweat', 'swimming', 'swordplay', 'table tennis', 'tanks',
    'tanned skin', 'teacher', "teens' love", 'tennis', 'tentacles',
    'terrorism', 'threesome', 'time manipulation', 'time skip', 'tokusatsu',
    'tomboy', 'torture', 'tragedy', 'trains', 'transgender', 'travel',
    'triads', 'tsundere', 'twins', 'urban', 'urban fantasy', 'vampire',
    'video games', 'vikings', 'villainess', 'virginity', 'virtual world',
    'volleyball', 'vore', 'voyeur', 'vtuber', 'war', 'watersports', 'werewolf',
    'witch', 'work', 'wrestling', 'writing', 'wuxia', 'yakuza', 'yandere',
    'youkai', 'yuri', 'zombie'
]
