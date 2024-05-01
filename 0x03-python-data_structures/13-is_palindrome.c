#include "lists.h"

/**
 * is_palindrome - Tells if a singly linked list is a palindrome or not.
 * @head: Address of the head pointer.
 *
 * Return: 1 if SLL is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int len, count;
	listint_t *current, *head2, *reversed;

	if (head == NULL)
		return (0);
	if (*head ==  NULL || (*head)->next == NULL)
		return (1);
	current = *head;
	reversed = malloc(sizeof(listint_t));
	if (reversed == NULL)
		return (0);
	reversed->next = NULL;
	head2 = reversed;
	len = count = 0;
	while (current != NULL)
	{
		reversed->n = current->n;
		if (reversed->n == (*head)->n)
			break;
		reversed = malloc(sizeof(listint_t));
		if (reversed == NULL)
			return (0);
		reversed->next = head2;
		head2 = reversed;
		current = current->next;
		len++;
	}
	while (count < len / 2)
	{
		if (head2->n == (*head)->n)
		{
			count++;
			head2 = head2->next;
			*head = (*head)->next;
			continue;
		}
		return (0);
	}
	return (1);
}
