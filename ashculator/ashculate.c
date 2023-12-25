/**
 * file: ashculate.c
 * date created: 25-Dec-2023
 * date updated: 25-Dec-2023
 * author: Emmanuel Enchill
 *
 * description: this file contains the main entry point for the
 * application
 *
 * Functions:
 * @main
 */

#include "ashculate.h"

/**
 * main - execute simple arithmetic computations
 *
 * Return: Always 0 (success)
 */
int main(void)
{
	size_t len = 0;
	int status;
	char *args = NULL;

	do {
		printf("ashculate ?> ");
		len = readLine(&args, len);
		if (strcmp(args, "exit\n") == 0)
			break;
		status = processInput(args);
	} while (status);
	
	free(args);

	return (0);
}
