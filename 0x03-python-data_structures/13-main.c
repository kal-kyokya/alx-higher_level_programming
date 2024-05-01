#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	print_listint(head);
	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n\n");
	else
		printf("Linked list is not a palindrome\n\n");
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	print_listint(head);
	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n\n");
	else
		printf("Linked list is not a palindrome\n\n");
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 24);
	print_listint(head);
	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n\n");
	else
		printf("Linked list is not a palindrome\n\n");
	free_listint(head);

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 5005);
	add_nodeint_end(&head, 10101);
	add_nodeint_end(&head, 925528);
	add_nodeint_end(&head, 1531999);
	add_nodeint_end(&head, 925528);
	add_nodeint_end(&head, 10101);
	add_nodeint_end(&head, 5005);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);
	print_listint(head);
	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n\n");
	else
		printf("Linked list is not a palindrome\n\n");
	free_listint(head);

	return (0);
}
