#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *crnt, *check;

	if (list == NULL || list->nxt == NULL)
		return (0);
	crnt = list;
	check = crnt->nxt;

	while (crnt != NULL && check->nxt != NULL
			&& check->nxt->nxt != NULL)
	{
		if (crnt == check)
			return (1);
		crnt = crnt->nxt;
		check = check->nxt->nxt;
	}
	return (0);
}
