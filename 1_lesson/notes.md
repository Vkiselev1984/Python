## ВВЕДЕНИЕ В АЛГОРИТМЫ И СТРУКТУРЫ ДАННЫХ НА PYTHON

У большинства задач можно выделить несколько вариантов решения, которые дают один и тот же результат, но при этом занимают разное время выполнения, по-разному потребляют память, отличаются по объему кода. Т.е. при запуске эти различных вариантов решений у вас не возникают синтаксические или семантические ошибки (когда задача дает результат, который и должна давать, например, 2+2=4), но решения эти отличаются именно по своим качественным характеристикам.

При этом, однозначно сказать какое решение эффективнее нельзя, поскольку в одним условиях нам важна в первую очередь скорость работы скрипта, а в других объем выделяемой памяти, в-третьих – объем кода.

Умение мысленно «разложить» задачу на составляющие является важным умением программиста-алгоритмизатора, для развития которого необходима постоянная практика.

Любой алгоритм проходит несколько стадий, от его вербального описания и псевдокода до реализации на языке программирования. Задача программиста-алгоритмизатора – понять, какие необходимо применить средства языка программирования для успешного воплощения алгоритма.

Освоить фундаментальные алгоритмы, не зависящие от языка реализации, например, решето Эратосфена, алгоритмы сортировки и т.д. Существуют алгоритмы, имеющие, например, математическое доказательство и практическую ценность при решении реальных задач. Эти фундаментальные алгоритмы можно «переложить» на различные языки программирования. Но прежде необходимо понять суть самих таких алгоритмов.

При решении задач важна не только семантическая правильность кода (программа должна давать ожидаемый результат), но и его стилевая корректность, т.е. соответствие стандарту PEP-8.

На тему анализа эффективности алгоритмов мы подробнее поговорим на уроках 4 и 6. Пока же нужно понять, что это действительно важно. При этом для оценки времени выполнения мы будем вычислять не только его абсолютные значения, но и описывать время выполнения с помощью нотации «О-большое».

Также мы обязательно узнаем, что, например, у многих стандартных операций, выполняемых над списками и словарями в Python, уже есть заранее известный вариант функции «О-большое».

## Начнем

Представим, у нас есть две программы, которые решают одну и ту же задачу. Как понять, что одна программа лучше другой?
Давайте вспомним, что алгоритм – это набор действий для решения задачи. Программа – это вариант того, как алгоритм переложен на язык программирования. Для одного и того же алгоритма мы можем написать множество версий программ, которые зависят от языка и разработчика, его индивидуальных особенностей написания кода.

Возьмем две простые функции, т.е. два алгоритма. Как определить какой из них эффективнее?

[Пример](/1_lesson/first_int_sum.py "Вычисление суммы первых n целых чисел")

Но эти две функции простые и без труда можно определить, что в одной из них есть лишние операции и код нужно немного оптимизировать. Здесь мы нашли решение быстро, мы обошлись без замеров, просто выполнили визуальный анализ кода. Но визуально оценивать эффективность кода мы можем только после большого опыта в программировании.

А что делать, если мы говорим о сложных, объемных скриптах?

Тогда нужно сказать, что лучшим будет тот, который наиболее эффективно использует ресурсы или ему их требуется меньше.
Соответственно, нужно найти такой алгоритм, но по каким критериям сравнивать алгоритмы?

Это прежде всего время и оперативная память, требуемые алгоритмы для решения задачи.

Как же измерить время? Воспользуемся самым простым способом – модулем time. Таким образом, мы сможем получить абсолютные цифры.

[Пример](/1_lesson/tuple.py "Замер времени операций")

Если мы запустим код на различных машинах, мы получим разное итоговое время. Даже, если запустить код несколько раз на одной машине, цифры все равно будут разные.

### Почему так?

Потому что цифры зависят от ресурсов конкретной машины (объема оперативной памяти), текущей загрузки процессора, разрядности ОС и даже версии интерпретатора.

Теперь понятно, что получать оценку времени в цифровом выражении не так уж эффективно. Хорошо было бы для оценки алгоритмов использовать характеристику, не привязанную к параметрам машины, параметрам ОС и интерпретатора. Но чтобы эта характеристика позволяла дать однозначный ответ, какой из алгоритмов более эффективный.

### Вот тут начинается самое интересное

Самое время перейти к О-нотации (нотация О-большое). Это подход непростой в понимании, но очень важный. Если взять научное определение, то это математическое обозначение для сравнения асимптотического поведения функций.

Или более простыми словами эта нотация описывает как увеличивается потенциальное время выполнения алгоритма с ростом размера решаемой задачи.

Что такое размер задачи? По сути это количество операций, выполняемых в алгоритме. Определять время выполнения этих операций в абсолютных цифрах, как уже стало понятно, дело необъективное. Цифры будут разными.

Выполнить подсчет операций в алгоритме это уже более реально и объективно, т.к. количество операций не привязывается к параметрам вычислительной машины.

Т.е. мы можем взять несколько алгоритмов и определить, как в них будет меняться количество операций в зависимости от изменения входящего объема данных, т.е. от изменения размера решаемой задачи.

Конечно мы не будем подсчитывать количество операций в цифрах, потому что входящий объем данных будет разным. И значит количество операций будет разным.

Нам нужно именно оценить алгоритмы с помощью некоторых формул, где не было бы привязки к цифрам, но совершенно точно было показано, как меняется количество операций алгоритма (а значит и его время) с ростом входящего объема данных.

Вот такое непростое на первый взгляд описание.

[Пример](/1_lesson/difficulty_check.py "Оценка сложности")

Приведенный алгоритм характеризуется квадратичной сложностью.

### Как мы это определили?

Сложили сложности отдельных выражений: T(n)=3+3n^2+2n+1=3n**2+2n+4

И выбрали то слагаемое выражения, которое оказывает наибольшее влияние на время выполнения всего скрипта (доминантную составляющую).

По сути под размером задачи здесь имеется в виду число операций алгоритма в зависимости от n. В других задачах зависимость может быть от размера массива или какого-либо другого объекта.

В таблице 1 приведено сравнение функций для нотации О-большое. Это и есть те самые обозначения, которыми мы должны описывать алгоритмы. Т.е. каждому алгоритму присуще какое-либо обозначение из этого перечня. Самое сложное конечно определить какое обозначение будет у нашего алгоритма.

![Таблица 1](/1_lesson/img/big_O.png "Наиболее распространные функции для O большого")

На рис. 1 показаны графики функций из таблицы.

![График](/1_lesson/img/chart_big_O.png "График роста O большого")

Основные варианты функций О-нотации и примеры задач под эти функции:

![Варианты](/1_lesson/img/variants_big_O.png "Варианты O большого")

### O(1) — постоянное время (константная сложность)

Главная особенность – каким бы ни был размер передаваемых в алгоритм данных, время его работы будет одним и тем же. Например, мы можем передать массив, в котором 5 или 1000 элементов – это никак не повлияет на производительность алгоритма.

[Сложность: O(1)](/1_lesson/o1.py "Сложность: O(1)")

Главная особенность – каким бы ни был размер передаваемых в алгоритм данных, время его работы будет одним и тем же. Например, мы можем передать массив, в котором 5 или 1000 элементов – это никак не повлияет на производительность алгоритма.

В данном случае, например, len() – это встроенная функция. Как мы узнали ее сложность?

Все стандартные операции и функции имеют заранее известную сложность. Где ее найти? Например, в таблицах 

![Таблица № 1](/1_lesson/img/img1.png "Таблица № 1")
![Таблица № 2](/1_lesson/img/img2.png "Таблица № 2")
![Таблица № 3](/1_lesson/img/img3.png "Таблица № 3")
![Таблица № 4](/1_lesson/img/img4.png "Таблица № 4")
![Таблица № 5](/1_lesson/img/img5.png "Таблица № 5")
![Таблица № 6](/1_lesson/img/img6.png "Таблица № 6")
![Таблица № 7](/1_lesson/img/img7.png "Таблица № 7")
![Таблица № 8](/1_lesson/img/img8.png "Таблица № 8")
![Таблица № 9](/1_lesson/img/img9.png "Таблица № 9")

### O(log n) — логарифмическое время

Главная особенность – время выполнения алгоритма определяется по формуле: логарифм от размера входных данных. Яркий пример – бинарный поиск, когда массив данных последовательно делится пополам до достижения результата – нахождения нужного элемента.

[Пример](/1_lesson/binary_search.py "Бинарный поиск")

### O(n) — линейное время

Главная особенность – время выполнения алгоритма прямо пропорционально размеру входящих данных. С ростом количества элементов в массиве растет и время выполнения алгоритма.

[Пример](/1_lesson/linear_complexity.py "Линейная сложность")

### O(n log n) — линейно-логарифмическое время

Главная особенность – объединяет черты линейной и логарифмической сложностей. В данном алгоритме также фигурирует подход «Разделяй и властвуй», как при логарифмической сложности, но массив сперва разбивается на подмассивы до тех пор, пока в каждом не будет по два элемента. Каждая пара сортируется, а далее отсортированные пары объединяются и продолжается сортировка полученного результата. Ярки пример алгоритма с такой сложностью – сортировка слиянием.

### O(n^2) — квадратичное время

Главная особенность – время выполнения алгоритма зависит от квадрата размера входных данных.

[Пример](/1_lesson/quadratic_complexity.py "Квадратичная сложность")

### O(2^n) — экспоненциальное время

Главная особенность – удваивание вычислений при добавлении очередного нового элемента в массив. Такую сложность можно наблюдать в рекурсивных алгоритмах – в тех, когда один вызов функции порождает еще два вызова этой же функции. Яркий пример – вычисление чисел Фибоначчи.

[Пример](/1_lesson/fibonacci_numbers.py "Экспоненциальное время")

### O(n!) — факториальное время

Главная особенность – время выполнения алгоритма растет факториально от размера входных данных. Яркий пример – обычная рекурсия. Здесь даже при небольшом росте входных данных, время выполнения алгоритма растет очень существенно.

[Пример](/1_lesson/traveling_salesman_task.py "Факториальное время")

## ФУНДАМЕНТАЛЬНЫЕ АЛГОРИТМИЧЕСКИЕ СТРУКТУРЫ ДАННЫХ

Это именно фундаментальные структуры данных, некоторые сложные системы, а не встроенные функции или классы. Структуры данных – это не списки, кортежи, словари и т.д, но они могут создаваться на основе списков, словарей и т.д.

### Стек данных

Под стеком понимается упорядоченная структура элементов. Вставка и удаление элементов строится по принципу LIFO – «последним пришёл - первым вышел». Таким образом, более новые элементы находятся ближе к вершине стек, старые – к основанию. Примеры стеков из жизни – стопка книг, тарелок и т.д.

![Stack](/1_lesson/img/stack.png "Stack")
![Stack](/1_lesson/img/stack2.png "Stack")

Со стеками мы сталкиваемся ежедневно. Например, в каждом веб-браузере существует кнопка «Назад». Когда мы перемещаемся от одной страницы к другой, URL-ы этих страниц помещаются в стек. Таким образом, текущая страница, занимает вершину, а самая первая из просмотренных – занимает основание. При нажатии кнопки «Назад» мы будем перемещаться по страницам в обратном направлении.

В программировании мы также очень часто имеем дело со стеками (рекурсия) или даже создаем их сами. Правда в случае с рекурсией мы говорим не о стеке данных. А о стеке вызовов.

Мы не создаем его сами, вручную, он уже заложен в библиотеку Python. Подробнее о стеке вызовов мы поговорим на уроке 2.
Сейчас же мы говорим о стеке данных, но это не встроенный класс. Как же тогда его создать, сымитировать? А как мы описываем собственные сущности? С помощью ООП.

Реализуем стек в виде класса. Стековые операции будут воплощены в его методах. Для реализации хранения элементов стека воспользуемся мощью примитивных коллекций, реализованных в Python. Будем использовать список. Но нужно определиться, какой из его концов будет являться вершиной стека, а какой – базой. После принятия решения можно приступать к реализации, опираясь на всем знакомые методы списков, в частности, append и pop.

[Пример](/1_lesson/stack_class.py "Класс стека")

### Применение стека

Стек данных (именно о нем мы говорим в этом уроке) может применяться при реализации алгоритмов в различных предметных областях, там, где необходимы возможности стека, например, при реализации алгоритмов парсинга, обхода сложных структур, деревьев, графов и т.д.

Рассмотрим один учебный пример использования стека, в котором мы реализуем конвертацию числа из десятичного формата в двоичный. Применим алгоритм «Разделяй на два», в котором стек позволяет запомнить цифры двоичного результата.

Мы простыми итерациями шаг за шагом разбиваем число в десятичном формате на два, далее получаем и записываем остаток в стек. У четного числа будет ноль в остатке и соответствующая цифра на первом месте. У нечетного числа в остатке наоборот будет единица и эта же цифра на первом месте.

![Stack](/1_lesson/img/stack3.png "Stack")

[Пример](/1_lesson/divide_by_two.py "Стек")

### Очередь

Под очередью понимается коллекция элементов, напоминающая конвейерную линию. Элементы добавляются в начало коллекции, а удаляются с конца. Это так называемый принцип FIFO, (first-in first-out).  Ещё он известен, как «первым пришёл - первым вышел».

![Очередь](/1_lesson/img/queue.png "Очередь")

В информатике тоже есть распространённые примеры очередей. В компьютерной лаборатории стоит 30 компьютеров, подключённых по сети к одному принтеру. Когда студенты хотят что-то распечатать, они набирают задание «встать в очередь» вместе со всеми другими ожидающими печати заданиями. Первое задание – следующее, которое будет выполнено. Если вы последний в очереди, то должны ждать, пока напечатаются все стоящие перед вами документы.

В Python очередь создадим аналогично стеку – через использование ООП и списков. Будем использовать функцию insert() для вставки элементов в очередь (в ее начало), а pop() для удаления переднего элемента. Так будет вполне удобно.

[Пример](/1_lesson/queue.py "Класс очереди")

Рассмотрим интересный пример использования очередей – алгоритм игры «Горячая картошка». По условиям данной игры участники выстраиваются в круг и перекидывают предмет от соседа к соседу. В определенный момент игры весь процесс останавливается и участник, у которого в руках остался предмет (картошка), покидает игру. Игра продолжается, пока не останется единственный победитель.

В нашем случае программа получает на вход набор имен и параметр num, применяемый для подсчета. Программа будет возвращать имя последнего участника, оставшегося после повторяющегося отсчета num.

Для имитации круга участников используем очередь. Представим, что игрок, который держит картошку, занимает первую позицию в очереди. Он перебрасывает картошку, мы извлекаем его из очереди и ставим обратно, но уже в хвост очереди. Далее игрок будет ждать, пока все, кто перед ним, побудут первыми, а затем вернется на указанное место снова. После выполнения num операций извлечений/постановок участник, находящийся впереди, удаляется окончательно и цикл повторяется сначала. Процесс повторяется до тех пор, пока размер очереди не станет равным 1, т.е. пока не останется один участник в очереди.

[Пример](/1_lesson/queue_hot_potato.py "Очредь")

### Дек

Под деком (или двусторонней очередью) понимается упорядоченный набор элементов. Его отличительная особенность заключается в том, что новые элементы можно добавить, и в «голову», и в «хвост». Аналогично, существующие элементы могут быть удалены из обоих концов. Это «гибрид» стека и очереди.

![Дек](/1_lesson/img/dek.png "Дек")

Реализуем дек на Python, как ранее, с использованием ООП.

[Пример](/1_lesson/deque.py "Дек класс")

Рассмотрим применение дека на примере решения задачи «палиндром». Это строка, которая одинаково читается с обеих сторон. Например, «молоко делили ледоколом». Мы обработаем строку слева направо и добавим каждый ее элемент по очереди в хвост дека.

![Дек](/1_lesson/img/dek2.png "Дек")

Т.к. мы можем удалить сразу два элемента, то можно выполнить их сравнение и продолжить только если символы совпадают. При соответствии первого и последнего в процессе всего решения, то мы в конце придем или к отсутствию символов или останемся с деком размером 1. В обоих случаях исходный набор символов (строка) будет палиндромом.

[Пример](/1_lesson/pal_checker.py "Дек")