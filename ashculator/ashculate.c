#include "ashculate.h"

/**
 * main - execute simple arithmetic computations
 *
 * Return: Always 0 (success)
 */
int main(void)
{
	INFO info[] = { INFO_T_INIT };
	int status;

	do {
		printf("ashculate ?> ");
		readLine(info);
		status = processInput(info);
	} while (status);

	free(info->args);

	return (0);
}
