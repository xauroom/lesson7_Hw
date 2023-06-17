// Задача 50. Напишите программу, которая на вход принимает
// значение элемента в двумерном массиве, 
// и возвращает позицию этого элемента
// или же указание, что такого элемента нет.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 17 -> такого числа в массиве нет

using System;

public static class Program
{
	public static void Main()
	{
		void FillArray(int[,] array)
		{
			for (int i = 0; i < array.GetLength(0); i++)
				for (int j = 0; j < array.GetLength(1); j++)
					array[i, j] = new Random().Next(-30, 31);
		}

		void PrintArray(int[,] array)
		{
			for (int i = 0; i < array.GetLength(0); i++)
			{
				for (int j = 0; j < array.GetLength(1); j++)
					Console.Write($"{array[i, j],3}    ");
				Console.WriteLine("");
			}
		}

		void PickElem(int[,] array)
		{
			System.Console.WriteLine("Введите значение искомого элемента:");
			int elem = Convert.ToInt32(Console.ReadLine());

			int pos1 = 0;
			int pos2 = 0;
			bool isElem = false;

			for (int i = 0; i < array.GetLength(0); i++)
			{
				for (int j = 0; j < array.GetLength(1); j++)
				{
					if (array[i, j] == elem)
					{
						pos1 = i;
						pos2 = j;
						isElem = true;
					}
				}
			}
			if (isElem)
			{
				System.Console.WriteLine($"({pos1},{pos2})");
			}
			else System.Console.WriteLine("такого числа в массиве нет");
		}

		Console.Clear();
		System.Console.WriteLine("Введите количество строк");
		int rows = Convert.ToInt32(Console.ReadLine());
		System.Console.WriteLine("Введите количество столбцов");
		int cols = Convert.ToInt32(Console.ReadLine());
		int[,] array = new int[rows, cols];
		FillArray(array);
		PrintArray(array);
		PickElem(array);
	}
}
