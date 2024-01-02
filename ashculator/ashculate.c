#include "ashculate.h"

void ashculateInfo(void) __attribute__((constructor));

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

/**
 * ashculateInfo - information about program
 *
 * Return: nothing
 */
void ashculateInfo(void)
{
	printf("***** ASHCulator 0.0.1 (Jan 02, 2024) *****\n");
	printf("Perform Basic BODMAS Arithmetic Computations\n\n");
}
