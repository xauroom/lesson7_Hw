// Задача 52. Задайте двумерный массив из целых чисел.
// Найдите среднее арифметическое элементов в каждом столбце.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.

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

		void EveryColAverage(int[,] array)
		{
			System.Console.Write("Среднее арифметическое каждого столбца: ");
			float[] avg = new float[array.GetLength(1)];
			for (int i = 0; i < array.GetLength(1); i++)
			{
				float sum = 0;
				for (int j = 0; j < array.GetLength(0); j++)
				{
					sum += array[j, i];
				}
				avg[i] = sum / array.GetLength(0);
				System.Console.Write($"{avg[i]} ");
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
		EveryColAverage(array);
	}
}
