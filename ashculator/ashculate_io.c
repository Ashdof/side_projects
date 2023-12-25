/**
 * file: ashculate_io.c
 * date created: 25-Dec-2023
 * date updated: 25-Dec-2023
 * author: Emmanuel Enchill
 *
 * description: this file contains functions that perform input
 * and output operations
 *
 * Functions:
 * @readLine
 */

#include "ashculate.h"

/**
 * readLine - read a line of input
 *
 * Return: the line of input read
 */
ssize_t readLine(char **line, size_t n)
{
	ssize_t len;

	len = getline(line, &n, stdin);
	if (len == -1)
	{
		if (feof(stdin))
			exit(EXIT_SUCCESS);
		else
		{
			perror("readline");
			exit(EXIT_FAILURE);
		}
	}

	return (len);
}
