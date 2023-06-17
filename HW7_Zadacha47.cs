// Задача 47: Задайте двумерный массив
// размером m×n, заполненный случайными
// вещественными числами.
// m = 3, n = 4.
// 0,5 7 -2 -0,2
// 1 -3,3 8 -9,9
// 8 7,8 -7,1 9

using System;

public static class Program
{
	public static void Main()
	{

		void FillArrayVesch(float[,] array)
		{
			for (int i = 0; i < array.GetLength(0); i++)
				for (int j = 0; j < array.GetLength(1); j++)
					array[i, j] = new Random().NextSingle() * 60 - 30;
		}

		void PrintArray(float[,] array)
		{
			for (int i = 0; i < array.GetLength(0); i++)
			{
				for (int j = 0; j < array.GetLength(1); j++)
					Console.Write($"{array[i, j],3}    ");
				System.Console.WriteLine();
			}
		}



		Console.Clear();
		System.Console.WriteLine("Введите количество строк");
		int rows = Convert.ToInt32(Console.ReadLine());
		System.Console.WriteLine("Введите количество столбцов");
		int cols = Convert.ToInt32(Console.ReadLine());
		float[,] array = new float[rows, cols];
		FillArrayVesch(array);
		PrintArray(array);
	}
}
