import re
from functools import reduce

puzzleInput = """.......................661.........................485..565.......344.......325.....................................841.....725.............
....*609..131................512.......................*................536*..............462/..-...60..424.........@....$.*................
.316.........*.......39..................@.630......377........919...........98................789..*..*..............788..2.......=..564...
...........431...535...*...............622.-..../.................*..........*.......682...........108.116....@...-...............299.......
.....................428.....378...844.........416...............586.537=..27..........*......$..............871...331..................492.
...878....390....%..............*.*...................739.496=.................867......867..867.........................344......487.../...
...../.....*...558........@..535...644..................+.........404..605.......*................................%.....*...................
........................381............729..726....578........10...*..........818..............................929....934..........119......
.53....31..........734-..........847*.................#.........*...........#............217............/..321....................*.........
.......=.............................509.315.654.................60.........925.747*559..*.....430....226..*...................290...848=...
..........=.......546......664..507......../....#.......337.............................94........=.........359....528*996..................
.....351...638.......*.............*433............337.....................226...859........../............................378..............
.......*..........648.........183.........126........*...........208.954......=....*.......626........499*..........803.../....642.235......
.518*...813..990..............*..............*......699...133....+...............68...............79......838.447...*..........*...*........
................+.696*.........586.6......243.............*..........$224.............392...275.....-.........*...699...#177..230.593.&.....
...........$326.......683.-761.......491......./.........26...........................*.....=.........56.305.262.......................150..
....=.......................................41.908.........................819.785.....276.....&.................%..........................
.618......401$...............-......................599..124......34+.........*..............676..................342...........473.........
....................889......888..454....723/.........*.................141*.....958.......................................416.....*94......
....212.............-................%.........826=....552..................569....*............................728........=............143.
...*......287...................=60.............................872.....886.......171....437......815..680.........*.............633....+...
..234....*.....687..........432........203/.....*...275.65.........*341.@...........................*....%.246......272.....922*..../.......
........967.........495.......*....161.......474.97...*..*..84.400.........*295....805......................@...................915.........
...419.................*.979...932....*.............729.215.#....*.......81........*......554.263*567..........812..........................
.....*..............458....$.........682......................179................348..906.................428.../............798............
...668..................-.........................552............./..................=.......+...........@..........99........*..85.4.......
........29......938..594......107........*171.98.....*..896....$..491...........+..........412..12.............326.*.....705..4....*........
..........*....................+......332......@....949..*...750.......$..974....342.............*....558......#............*..........794..
.......459....342*.........637...........................273.....658..601....*................735....*...............%....627....889...*....
.697..............131....................718.................689.............450....390............994.............793.............*..241...
..............991........89..........14.......*.................*912.............39.+...698.............................953*240...87........
..324.............618.....*...328......*....538.%.....307.920.........515...............*...................................................
.....*386...........*...780..*.......475.........719...*...*...................910...410................384.....999........*756.............
....................268.......701.............72........63.43...193.....+..................674...670$....*........*......95.......893.......
...16.........................................*....663........../....407.....................*........258....264=.298........202*..../......
...&......574................187.......88...53.........931........@......&759....$..672....385..............................................
.....938........192......297....*.723...*.................%......930...........692................283.....................=349.........&981.
......*....................&.207....*...843.736.........................260..........677..389........*..............954..........&..........
......603........713.............745..................411.359.922.......*.............*......*.......718..888..561..=.........182..206......
............896....*.....173*383.......%...145...943...*.....*.........622..382*.......180.141............*...........................*.....
.....89........*...238.............+.714....*........575../.........................@...............$.....539.......114*721.645........471..
.......*307....968..............250......836.....498......59....909..601*..........117...........435../........944..........................
............*...............56*.................+....498..........-......730.882..........975..........680........*...95......152....$517...
...........150.......142.......473.713.+262...........=...577.266...736..........668..$.........70*111......811.165..@......................
.......741.............*.97.......................=.........*.......*....-654..........428..157................................748*823......
.........*............48...*.....772....892.....350....$.....760.148.............................440...........731*563......................
........260..............227...............*..........795..................649.....27.107...219.@.....23@...............226......369........
...41............&...................+...136.....546.......$.920...................+...*...&....../.........981...........@.......*.....454.
...*......635%....782...............560............*....896...........854..+...........694......340...@.498*....................41..959*....
...486..........................63..................810......641....+....*..532....642.......$.......90.....................76=.............
..........325.....................@..............@...........-....539.407.............$......9...........550................................
...787..$....*.$105.126.+810.........497.576...538.............................718.......................*...+....317..519..................
.......303.493...........................................-...........462..647..*...........%..+875....641..644.....*......*.....154.588.....
................./.....-......44.........%...@140.......228...43......*....*..132.794...628.......................669....110....*.....*.....
....579...........348..32.491*.......#...646.......506..........*708......74........#........117..............24*............698....532.....
......*.........................902.722............=....=........................................700....610......878....*...................
.../..885.../..351.............*.........................799.....814*238......*339....428*825......./................965.862......125.......
.723......243.@........852..........757...784.472..814.......603...........151........................279.617....849........................
........................*......./............*.......*.........*....#.............91.......246...384.....*........%.........................
.218.659....113+........128....691...................972......571....934............*......*...................................442..236.....
....*...............455.............868......&379.........................594.......80....654.....................421.456...................
............2*535......*410...553........409......235.173..779......116.....*.................&........*646.418*.....*.................596..
.70#.361......................./....493....$..........*...-.....440.........317...865...323....696..202..........952.......187.....%....#...
..........%...767......318............*................1.............../...........*......*................241......@.147...*.....389.......
..921.....301..*........*............67.540.../....149.........=........827.....=.347....956..........980...............$...204.............
...*............341......154.............*..695.....$.....20.183..............177..................$...$...66......699..........495......296
.460........&.......+............%.......4......+........*.......................................347.........*36...*....912.......*..765....
............142..163......885..480...............805.%...587...........289.310*389........$843..........-..........417....*.....628....*....
.............................*............434........803........482......-.........556.........&.........294...33$.........79........358....
.......................407@...873...............+..................*542....../.41....$./758....176.................*........................
.........842......................442*766.......284.........842...........856...*......................647......422.94..............@.......
....$........799............................&.......433.318*.....576..........111....................................................788....
.720...168.....%........840..............989....................*.......=............468..419...........198.................................
......*..................+..392..............282.......&...............591..........&....*....101.340....-.....187.....-....................
.....746...........................499...779...*....456...........@....................346....*......%...........*..693.......94..72........
.........970..671..696./....................&..999......124..246.434...........................173........@.....165.......925*.../..........
..628.............*....608.....827-.......*..............#....*........634...../418......185.......311...808.........372*............824....
..........694...360.....................43.645.................935........*516...........*....555.....*..................33.........-.......
............*............+........576#.........810*592..740.....................#665..968........*499.775..882+..............998............
....=303.....433.280......147..82.........................*..............................................................751*...............
.................$......................608...560..827...227....................448*..@......................@529.376...........@...........
...........465.....#.............554.....#.......#..#.......................401.......714...../.192.999..................466...28.161....351
..............&....706..157.679.@..........741..............818.811=..............412.......376...&..*.......=..............................
.441.....955....63.........*........=........+.............*..............#..........*..............399.......613.......444........*972.....
........@......*..................697..........600.&965...354.#.....392...827..665....326.................323...........&.......483.........
................381........972..........373*..*................9...&...........................289.........*................................
...........................*....+.............239......................863....................*..........341.....*329...................$...
801..+...638.659........358...29..695.....@........241...680.....863..........................310.#...........941........@216........311....
...*.358.*...*....................@....786....*330................&.........842........11..........279...................................686
.932..........666....533..712..............801.............64.544.....*972.....*353....-..809...........524...........397...............*...
.........795+.......*.......*......394=................586......*.........................................&...........................562...
...................629.......184........796..............=................-946.348.../670............63.........%...........................
.....428-................918.........@..............#.............850.889.........*..............673..#..110.221..........337.560...-.......
.....................926*.........809.........=......627.............*..........344..........343.*........*.......832.......*....*...216....
.....624.....+................................78............915..701.....876.........734.402.....181.193.460.639.....*...558...138..........
.../...*...91....804..324..985......#429......................*..*.............892....................*......*...321.727...........134......
...991............*.........*.............39...........%.633.213.623..........&...........601.919.....378.318...*............@34............
........183.....#.399...+..297..973...622..*........855../......................+684../......*................335.................733.......
..........@..576......597........*.....*....686....................371..98..23$......119................................=.777......*........
.................901%......*...412......102...........754...332.47*......*......861+......539................495@....801...*..404...777.....
.........577..........577..978.................990......*...#............236.............@..............339............../......*........534
..169.....*..687........*..........598..........*..349@.723.....864..........972............196.....491*........$........335.372............
.........339..=......633........29...*.........4............251*.....$..........*.250.........$.908..............356.230...........324.386..
.................943.............-.....=............................325...726.690.*................/.......646........*...214.......=.......
.........&468.......*..................999.......944.........751..........*.......219.837.107..............*...=....271..*..............283.
......*..........210.....*390.....917*.....996*.....+..790...-.........128...............*................905.277.......320....936..835.....
...640.581....*.......167.............392......29......*..........885............................369..................&...........*.$...#...
..............708..........106.223...................817.........*............277.........&.........@..795.-296....172..........633......229
.......82..........@679.......*....*806.................../....10.............*.........456...........*.................95...........3......
..........536....................12........=914..458.......214..........995..97.-735........370.......334..876=.........*.......950#........
.........*.............=.....10.......837...........+..518.................*...................*........................761.................
......414..=.........794.............=................*...................813.394...815.718....759........403...............738.............
............463...........-..238.419............810.41...........452..2=..................&..............&........435.................468...
........................103....*..........................+...11.&....................927...........%.......282...*...234.....229......*....
......301+....................678............100.......954.....*...@....182....@.........*....737...916....-....890....@..118*.......625....
............67...312..865+.............910.....*...382.......516....973....*..874.500..153.....*............................................
.....373+...*.....*...............979..........469....*375..............765...................99....................733................897..
..........828.....669......=.....*...........................................284.189...$..371......*168..............%.......762............
..........................4..565.226........562@....190......281....257.......*.......889./......57........./...#.......210..*..............
......47.......120.............#...................*...........&....*.....169.549............%............414..744......%....503.#208.......
........*.................643.........397...........350..........289....&...*........&.....323.....+..................................856...
.....*...............458....#........................................104.....931..855..............89..469.....882...........=.........*....
..594.777......390...*...........422........355..............654............................81........*...........*......282..630....195....
..................*.568.912........*........*.....377..........*......*877.............419..*.....148.768.......471....+....*...............
.......393......163..........298.820............@..................582.......823......=...........*....................952..................
..........*268.......*733.59...@.............403..........................................14&...502...............481.........$.....231.....
........#.........970.....*......#....981...........711.261=.................=.......................701..244................323.....*......
.396....993.............557.......46.....*...........+..........714*659.....134........623..........*............677.730..............846...
......#......91...405........296..........295..............@..*.......................#..............740............*........%..............
.......345..=........-.792....*..834................100.891....764...697........570......*....620*.@.....................508..295...........
...*13................../...340...#..134..............#................*..........*.......247......660....607....705.....=...........165....
.........521..824...222.............*......372..290.....844.825-.......867..820...627...........................*............128...../...777
...629...*....#..................788...535....*..-.......*.........361......................*......805.......732....914....../...-......@...
...*.....743...........853..................637.......880...-..849*........425............946..590....*302...........*.........748..........
...120.%.......271..............862.....70................207................=......233.......*..................443..263...................
........680....../.825.....&793...........*....................-720.............555........184..509.......22......*.............811.........
..........................................772.272......................134.........*..374.........*............573........*.......*.........
934..231.....*....821...230.....981..............%........707..370....*.....634%..787..*..........93..909..70..........199.59...490.........
.......*....525.........-........*...747...676=..../.......*..........829...............324..952.........%...*..........................%...
.....189.........................791.............236........687.868........................................505..............713......777...."""

testInput = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

#from: https://www.composingprograms.com/pages/16-higher-order-functions.html#currying
def curry2(f):
        """Return a curried version of the given two-argument function."""
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g

def curryWith(f, aParam):
    return curry2(f)(aParam)

def firstOfTuple(tuple):
    return tuple[0]

def secondOfTuple(tuple):
    return tuple[1]

def groupAndSpan(match):
    return match.group(1), match.span(1)

def span(groupAndSpan):
    return secondOfTuple(groupAndSpan)

def group(groupAndSpan):
    return firstOfTuple(groupAndSpan)

def groupNotEmpty(groupAndSpan):
    return group(groupAndSpan) != ''

def groupNotDot(groupAndSpan):
    return group(groupAndSpan) != '.'

def combinedAsTupleTakeOccurenceAsRangeAndNumber(groupAndSpan):
    return range(firstOfTuple(span(groupAndSpan)), secondOfTuple(span(groupAndSpan))), group(groupAndSpan)

def parseNumbers(s) :
    return list(
                map(combinedAsTupleTakeOccurenceAsRangeAndNumber, 
                    filter(groupNotEmpty, 
                           map(groupAndSpan, 
                               re.finditer('(\d*)', s)))))

def combinedAsTupleTakeLargerOccurenceAsRangeAndNumber(s, groupAndSpan):
    return range(max(0, firstOfTuple(span(groupAndSpan)) - 1), min(len(s), secondOfTuple(span(groupAndSpan)) + 1)), group(groupAndSpan)

def parseSymbols(s):
    return list(
                map(
                    curryWith(combinedAsTupleTakeLargerOccurenceAsRangeAndNumber, s), 
                    filter(groupNotDot, 
                           map(groupAndSpan, 
                               re.finditer('(\D{1})', s)))))

def numberOf(tuple):
    return int(secondOfTuple(tuple))

def rangeOf(tuple):
    return firstOfTuple(tuple)

def eachRowMergedWithPreviousCurrentAndNextRow(rows):
    return list(map(lambda row: 
                        (rows[row - 1].copy() if row > 0 else []) + 
                        (rows[row].copy()) +
                        (rows[row + 1].copy() if (row + 1) < len(rows) else []),
                    range(0, len(rows))))

def isOverlapping(ra, rb):
    return ra[-1] >= rb[0] and rb[-1] >= ra[0]

def areAnyRangesOverlapping(ranges, otherRange):
    return any(
                map(
                    curryWith(isOverlapping, otherRange), 
                    ranges))

def add(a, b):
    return a + b

def flatten(matrix):
     return list(reduce(add, matrix, [])) 

def part1(s) :
    lines = s.splitlines()
    numbers = list(map(parseNumbers, lines))
    symbols = list(map(parseSymbols, lines))
    eachSymbolRowMergedWithPreviousCurrentAndNext = eachRowMergedWithPreviousCurrentAndNextRow(symbols)

    numberTuplesAdjacentToAnyOfTheSymbols = []

    for row in range(0, len(lines)) :
        numberTuplesAdjacentToAnyOfTheSymbols.append(list(filter(lambda number: areAnyRangesOverlapping(map(rangeOf, eachSymbolRowMergedWithPreviousCurrentAndNext[row]),
                                                                                                        rangeOf(number)), 
                                                                numbers[row])))
    
    return reduce(add, map(numberOf, flatten(numberTuplesAdjacentToAnyOfTheSymbols)))

print(part1(testInput)) #4361
print(part1(puzzleInput)) #519444
