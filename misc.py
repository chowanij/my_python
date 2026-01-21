#!/usr/bin/env python3


def list_scope_issue(items=[]):
    items.append(1)
    return items

def main():
    list_scope_issue()
    list_scope_issue()
    result = list_scope_issue()
    print (f'{result}')


if __name__ == "__main__":
    main() 