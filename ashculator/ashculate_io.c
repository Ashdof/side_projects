#include "ashculate.h"

/**
 * readLine - read a line of input
 * @info: a pointer to a space in memory to store data
 *
 * Return: the line of input read
 */
ssize_t readLine(INFO *info)
{
	ssize_t len;

	len = getline(&info->args, &info->len, stdin);
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
