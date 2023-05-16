{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Numpy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Материалы:\n",
    "* Макрушин С.В. \"Лекция 1: Библиотека Numpy\"\n",
    "* https://numpy.org/doc/stable/user/index.html\n",
    "* https://numpy.org/doc/stable/reference/index.html"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Задачи для совместного разбора"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Сгенерировать двухмерный массив `arr` размерности (4, 7), состоящий из случайных действительных чисел, равномерно распределенных в диапазоне от 0 до 20. Нормализовать значения массива с помощью преобразования вида  $𝑎𝑥+𝑏$  так, что после нормализации максимальный элемент масcива будет равен 1.0, минимальный 0.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1.87075604  5.80698623 10.43891259  2.28231465  3.23758749  6.08561646\n",
      "   7.04129339]\n",
      " [ 9.06216228 18.93702693  3.45115162  7.8824202   6.00049585 12.03135076\n",
      "   6.62387362]\n",
      " [ 1.20884232 10.24714207 11.04840699  6.29010304  8.97997808  7.25116414\n",
      "   1.89296543]\n",
      " [ 0.18223429 14.61874161 15.33751617  7.74798969 19.49739957  4.5666768\n",
      "   6.40310885]] \n",
      "\n",
      "[[0.08741948 0.2912091  0.53101685 0.10872702 0.15818416 0.30563457\n",
      "  0.35511263]\n",
      " [0.45973865 0.97098794 0.16924097 0.39866011 0.30122763 0.61346182\n",
      "  0.33350164]\n",
      " [0.05315036 0.52108836 0.56257208 0.31622141 0.45548374 0.36597822\n",
      "  0.08856932]\n",
      " [0.         0.74741826 0.78463123 0.39170027 1.         0.22699482\n",
      "  0.32207203]]\n"
     ]
    }
   ],
   "source": [
    "a = np.random.uniform(0, 20,(4, 7))\n",
    "\n",
    "print(a,'\\n')\n",
    "\n",
    "a = (a-a.min())/(a.max()-a.min())\n",
    "\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Создать матрицу 8 на 10 из случайных целых (используя модуль `numpy.random`) чисел из диапозона от 0 до 10 и найти в ней строку (ее индекс и вывести саму строку), в которой сумма значений минимальна."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[6 4 0 0 3 7 6 2 5 1]\n",
      " [1 1 8 6 6 0 5 8 8 6]\n",
      " [3 0 4 0 4 5 2 5 0 6]\n",
      " [9 3 2 2 0 4 6 5 3 8]\n",
      " [5 0 0 6 0 4 1 0 0 9]\n",
      " [0 7 5 4 1 9 6 9 4 6]\n",
      " [6 3 9 1 0 2 2 3 5 4]\n",
      " [4 8 6 5 8 6 5 1 6 9]] \n",
      "\n",
      "[34 49 29 42 25 51 35 58] \n",
      "\n",
      "[5 0 0 6 0 4 1 0 0 9] 4\n"
     ]
    }
   ],
   "source": [
    "a = np.random.randint(0, 10, size = (8, 10))\n",
    "\n",
    "print(a,'\\n')\n",
    "\n",
    "b = np.sum(a, axis = 1)\n",
    "\n",
    "print(b,'\\n')\n",
    "\n",
    "print(a[b.argmin()],b.argmin())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Найти евклидово расстояние между двумя одномерными векторами одинаковой размерности."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as pl\n",
    "from mpl_toolkits.mplot3d import Axes3D\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of dimensions\n",
      "3\n",
      "2.9994048274562295\n"
     ]
    }
   ],
   "source": [
    "size = int(input('Enter number of dimensions\\n'))\n",
    "\n",
    "A,B = np.random.random(size)*size,np.random.random(size)*size #some vectors\n",
    "\n",
    "ans = np.linalg.norm(A-B)\n",
    "\n",
    "print(ans)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. Решить матричное уравнение `A*X*B=-C` - найти матрицу `X`. Где `A = [[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]]`, `B=[[3, -1], [2, 1]]`, `C=[[7, 21], [11, 8], [8, 4]]`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1.00000000e+00  5.55111512e-16]\n",
      " [-2.00000000e+00  1.00000000e+00]\n",
      " [ 3.00000000e+00 -4.00000000e+00]]\n"
     ]
    }
   ],
   "source": [
    "A = np.array([[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]])\n",
    "B=np.array([[3, -1], [2, 1]])\n",
    "C=np.array([[7, 21], [11, 8], [8, 4]])\n",
    "\n",
    "X = np.matmul(np.matmul(np.linalg.matrix_power(A,-1),-C),np.linalg.matrix_power(B,-1))\n",
    "\n",
    "print(X)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Лабораторная работа №1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Замечание: при решении данных задач не подразумевается использования циклов или генераторов Python, если в задании не сказано обратного. Решение должно опираться на использования функционала библиотеки `numpy`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. Файл `minutes_n_ingredients.csv` содержит информацию об идентификаторе рецепта, времени его выполнения в минутах и количестве необходимых ингредиентов. Считайте данные из этого файла в виде массива `numpy` типа `int32`, используя `np.loadtxt`. Выведите на экран первые 5 строк массива."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2. Вычислите среднее значение, минимум, максимум и медиану по каждому из столбцов, кроме первого."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "3. Ограничьте сверху значения продолжительности выполнения рецепта значением квантиля $q_{0.75}$. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "4. Посчитайте, для скольких рецептов указана продолжительность, равная нулю. Замените для таких строк значение в данном столбце на 1."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "5. Посчитайте, сколько уникальных рецептов находится в датасете."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "6. Сколько и каких различных значений кол-ва ингредиентов присутвует в рецептах из датасета?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "7. Создайте версию массива, содержащую информацию только о рецептах, состоящих не более чем из 5 ингредиентов."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "8. Для каждого рецепта посчитайте, сколько в среднем ингредиентов приходится на одну минуту рецепта. Найдите максимальное значение этой величины для всего датасета"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "9. Вычислите среднее количество ингредиентов для топ-100 рецептов с наибольшей продолжительностью"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "10. Выберите случайным образом и выведите информацию о 10 различных рецептах"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "11. Выведите процент рецептов, кол-во ингредиентов в которых меньше среднего."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "12. Назовем \"простым\" такой рецепт, длительность выполнения которого не больше 20 минут и кол-во ингредиентов в котором не больше 5. Создайте версию датасета с дополнительным столбцом, значениями которого являются 1, если рецепт простой, и 0 в противном случае."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "13. Выведите процент \"простых\" рецептов в датасете"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "14. Разделим рецепты на группы по следующему правилу. Назовем рецепты короткими, если их продолжительность составляет менее 10 минут; стандартными, если их продолжительность составляет более 10, но менее 20 минут; и длинными, если их продолжительность составляет не менее 20 минут. Создайте трехмерный массив, где нулевая ось отвечает за номер группы (короткий, стандартный или длинный рецепт), первая ось - за сам рецепт и вторая ось - за характеристики рецепта. Выберите максимальное количество рецептов из каждой группы таким образом, чтобы было возможно сформировать трехмерный массив. Выведите форму полученного массива."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[127244     60     16]\n",
      " [ 23891     25      7]\n",
      " [ 94746     10      6]\n",
      " [ 67660      5      6]\n",
      " [157911     60     14]]\n",
      "(100000, 3)\n"
     ]
    }
   ],
   "source": [
    "# 1 задание\n",
    "a = np.loadtxt('minutes_n_ingredients.csv',delimiter=',',dtype=np.int32,skiprows=1)\n",
    "\n",
    "print(a[:5],a.shape,sep='\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2.16010017e+04 9.05528000e+00] [2147483647         39] [0 1] [40.  9.]\n"
     ]
    }
   ],
   "source": [
    "# 2 задание\n",
    "\n",
    "b = a[:,1:]\n",
    "\n",
    "avg,mx,mn,med = np.average(b,axis=0),np.max(b,axis=0),np.min(b,axis=0),np.median(b,axis=0)\n",
    "\n",
    "print(avg,mx,mn,med)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(100000, 3)\n",
      "[[127244     60     16]\n",
      " [ 23891     25      7]\n",
      " [ 94746     10      6]\n",
      " ...\n",
      " [498432     65     15]\n",
      " [370915      5      4]\n",
      " [ 81993     65     14]]\n"
     ]
    }
   ],
   "source": [
    "# 3 задание\n",
    "q = np.quantile(a[:,1], q=0.75)\n",
    "\n",
    "a[:,1]=a[:,1].clip(max=q)\n",
    "\n",
    "print(a.shape,a,sep='\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "479\n",
      "[[127244     60     16]\n",
      " [ 23891     25      7]\n",
      " [ 94746     10      6]\n",
      " ...\n",
      " [498432     65     15]\n",
      " [370915      5      4]\n",
      " [ 81993     65     14]]\n"
     ]
    }
   ],
   "source": [
    "# 4 задание\n",
    "q = a[:,1]==0\n",
    "\n",
    "count = np.where(q)[0].size\n",
    "\n",
    "a[:,1][q] = 1\n",
    "        \n",
    "print(count,a,sep='\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100000\n"
     ]
    }
   ],
   "source": [
    "# 5 задание\n",
    "number_of_uniques = np.unique(a,axis=0).shape[0]\n",
    "\n",
    "print(number_of_uniques)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
      "       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,\n",
      "       35, 37, 39]), array([   13,   926,  2895,  5515,  7913,  9376, 10628, 10951, 10585,\n",
      "        9591,  8297,  6605,  4997,  3663,  2595,  1767,  1246,   790,\n",
      "         573,   376,   217,   161,   105,    69,    50,    28,    16,\n",
      "          16,    12,    12,     3,     1,     2,     1,     3,     1,\n",
      "           1], dtype=int64))\n",
      "37\n"
     ]
    }
   ],
   "source": [
    "# 6 задание\n",
    "uniques = np.unique(a[:,2],return_counts=True)\n",
    "\n",
    "print(uniques,uniques[0].size,sep='\\n')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(17262, 3)\n"
     ]
    }
   ],
   "source": [
    "# 7 задание\n",
    "q = a[:,2]<=5\n",
    "\n",
    "ingredients_not_gerater_than_five = a[np.where(q)]\n",
    "\n",
    "print(ingredients_not_gerater_than_five.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.26666667 0.28       0.6        ... 0.23076923 0.8        0.21538462]\n",
      "24.0\n"
     ]
    }
   ],
   "source": [
    "# 8 задание\n",
    "\n",
    "avg_ing_per_minute = a[:,2]/a[:,1]\n",
    "\n",
    "maximum = avg_ing_per_minute.max()\n",
    "\n",
    "print(avg_ing_per_minute,maximum,sep='\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9.96\n"
     ]
    }
   ],
   "source": [
    "# 9 задание\n",
    "\n",
    "avg_n_ings_for_top_100_longest_in_cooking = np.average(a[np.argpartition(a[:,1],-100)[-100:]],axis = 0)[2]\n",
    "\n",
    "print(avg_n_ings_for_top_100_longest_in_cooking)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[238462      5      3]\n",
      " [ 30541     40      9]\n",
      " [246486     65     11]\n",
      " [138400     65     13]\n",
      " [292402     65     11]\n",
      " [337396     45      7]\n",
      " [261673      2     10]\n",
      " [151038     65      8]\n",
      " [396023     15      4]\n",
      " [ 49696     10      5]]\n"
     ]
    }
   ],
   "source": [
    "# 10 задание\n",
    "\n",
    "print(a[np.random.choice(a.shape[0], 10, replace=False)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "58.802\n"
     ]
    }
   ],
   "source": [
    "# 11 задание\n",
    "q = a[:,2] < avg[1]\n",
    "\n",
    "percentage = 100*a[q].shape[0]/a.shape[0]\n",
    "\n",
    "print(percentage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[127244     60     16      0]\n",
      " [ 23891     25      7      0]\n",
      " [ 94746     10      6      0]\n",
      " ...\n",
      " [498432     65     15      0]\n",
      " [370915      5      4      1]\n",
      " [ 81993     65     14      0]]\n"
     ]
    }
   ],
   "source": [
    "# 12 задание\n",
    "ds = np.concatenate((a,np.array([[int(i<=20 and k<=5) for i,k in a[:,1:]]]).T),axis=1)\n",
    "\n",
    "print(ds)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9.552\n"
     ]
    }
   ],
   "source": [
    "# 13 задание\n",
    "q = ds[:,3] == 1\n",
    "\n",
    "percentage_of_simples = 100*a[q].shape[0]/a.shape[0]\n",
    "\n",
    "print(percentage_of_simples)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(3, 7588, 3)\n"
     ]
    }
   ],
   "source": [
    "# 14 задание\n",
    "\n",
    "# Если я правильно понял задание, в результате у нас должен бытть трехмерный массив, в котором изначальный массив разбит на группы по длине приготовления\n",
    "# тогда размеры итогового массива будут равны (3, <макс. кол-во рецептов для 3д массива>, 3)\n",
    "\n",
    "short = a[:,1] < 10\n",
    "standart = np.all([a[:,1] > 10,a[:,1] < 20],axis = 0)\n",
    "long = a[:,1] >= 20\n",
    "\n",
    "short_arr = a[short]\n",
    "standart_arr = a[standart]\n",
    "long_arr = a[long]\n",
    "\n",
    "\n",
    "max_ings = min(short_arr.shape[0],standart_arr.shape[0],long_arr.shape[0])\n",
    "\n",
    "list_3D = np.stack((short_arr[:max_ings],standart_arr[:max_ings],long_arr[:max_ings]),axis=0)\n",
    "\n",
    "print(list_3D.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}