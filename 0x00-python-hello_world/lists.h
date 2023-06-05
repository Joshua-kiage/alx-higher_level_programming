#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @i: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for ALX(0x00-python-hello_world) project
 */
typedef struct listint_s
{
	int i;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
listint_t *add_nodeint(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
int check_cycle(listint_t *list);

#endif
