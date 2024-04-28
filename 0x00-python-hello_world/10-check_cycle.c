#include "lists.h"

#define TRUE 1

/**
 * check_cycle - Tells whether a Singly linked list is looped or not.
 * @head: Pointer to the head node of the SLL.
 *
 * Return: 0 if no loop, 1 otherwise.
 */
int check_cycle(listint_t *head)
{
	listint_t *hare, *turtle;

	if (head == NULL || head->next == NULL)
		return (0);
	hare = turtle = head;
	while (TRUE)
	{
		turtle = turtle->next;
		hare = hare->next;
		if (hare->next == NULL)
			break;
		hare = hare->next;
		if (hare == turtle)
			return (1);
	}

	return (0);
}
