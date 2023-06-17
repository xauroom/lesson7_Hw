// Задача 2 HARD необязательная.
// Считается за четыре обязательных )
// то есть три этих и одна с будущего семинара
// Сгенерировать массив случайных целых чисел
// размерностью m*n (размерность вводим с клавиатуры)
// причем чтоб количество элементов было четное.
// Вывести на экран красивенько таблицей.
// Перемешать случайным образом элементы массива,
// причем чтобы каждый элемент гарантированно
// и только один раз переместился на другое место
// и выполнить перемешивание за m*n / 2 итераций

using System;

public static class Program
{
	public static void Main()
	{
		void FillArray(int[,] array)
		{
			for (int i = 0; i < array.GetLength(0); i++)
				for (int j = 0; j < array.GetLength(1); j++)
					array[i, j] = new Random().Next(-9, 10);
		}

		void PrintArray(int[,] array)
		{
			for (int i = 0; i < array.GetLength(0); i++)
			{
				for (int j = 0; j < array.GetLength(1); j++)
					Console.Write($"{array[i, j],3}    ");
				System.Console.WriteLine();
			}
		}

		void ParoGenerator(int[,] array)
		{
			int rows = array.GetLength(0);
			int cols = array.GetLength(1);
			int[,] positions = new int[rows * cols, 2];
			Random rnd = new Random();
			int index = 0;
			for (int i = 0; i < rows; i++)
			{
				for (int j = 0; j < cols; j++)
				{
					int row = rnd.Next(rows);
					int col = rnd.Next(cols);
					while (row == i && col == j)
					{
						row = rnd.Next(rows);
						col = rnd.Next(cols);
					}
					positions[index, 0] = row;
					positions[index, 1] = col;
					index++;
				}
			}
			int temp;
			for (int i = 0; i < positions.GetLength(0); i += 2)
			{
				int i1 = positions[i, 0];
				int j1 = positions[i, 1];
				int i2 = positions[i + 1, 0];
				int j2 = positions[i + 1, 1];
				temp = array[i1, j1];
				array[i1, j1] = array[i2, j2];
				array[i2, j2] = temp;
				Console.WriteLine($"{i / 2 + 1}-я итерация");
				PrintArray(array);
			}
		}

		Console.Clear();
		System.Console.WriteLine("Введите количество строк");
		int rows = Convert.ToInt32(Console.ReadLine());
		if (rows % 2 != 0) System.Console.WriteLine("Введите четное количество столбцов");
		else System.Console.WriteLine("Введите количество столбцов");
		int cols = Convert.ToInt32(Console.ReadLine());
		int[,] array = new int[rows, cols];
		FillArray(array);
		Console.WriteLine("Исходный массив");
		PrintArray(array);
		ParoGenerator(array);
	}
}
