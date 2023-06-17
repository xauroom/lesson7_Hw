// Задача HARD SORT необязательная. Считается за три обязательных
// Задайте двумерный массив из целых чисел.
// Количество строк и столбцов задается с клавиатуры.
// Отсортировать элементы по возрастанию слева направо
// и сверху вниз.
// Например, задан массив:
// 1 4 7 2
// 5 9 10 3
// После сортировки
// 1 2 3 4
// 5 7 9 10

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

		void SortUp(int[,] array)
		{
			int len = array.GetLength(0) * array.GetLength(1);
			int[] sort = new int[len];

			for (int i = 0; i < array.GetLength(0); i++)
			{
				for (int j = 0; j < array.GetLength(1); j++)
					sort[j + (i * array.GetLength(1))] = array[i, j];
			}
			System.Console.WriteLine("");

			int temp;
			for (int i = 0; i < len - 1; i++)
			{
				for (int j = i + 1; j < len; j++)
				{
					if (sort[i] > sort[j])
					{
						temp = sort[i];
						sort[i] = sort[j];
						sort[j] = temp;
					}
				}
			}

			for (int i = 0; i < array.GetLength(0); i++)
			{
				for (int j = 0; j < array.GetLength(1); j++)
					array[i, j] = sort[j + i * (array.GetLength(1))];
			}
		}

		Console.Clear();
		System.Console.WriteLine("Введите количество строк");
		int rows = Convert.ToInt32(Console.ReadLine());
		System.Console.WriteLine("Введите количество столбцов");
		int cols = Convert.ToInt32(Console.ReadLine());
		int[,] array = new int[rows, cols];
		FillArray(array);
		PrintArray(array);
		System.Console.WriteLine("");
		SortUp(array);
		System.Console.WriteLine("");
		PrintArray(array);
	}
}
