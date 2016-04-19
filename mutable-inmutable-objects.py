import timeit


def slow_string_concat(container):
    string_build = ""
    for data in container:
        string_build += str(data)
    return string_build


def test_slow_string_concat():
    slow_string_concat([x for x in xrange(100)])


def fast_string_concat(container):
    return "".join([str(data) for data in container])


def test_fast_string_concat():
    fast_string_concat([x for x in xrange(100)])


print(timeit.timeit(test_slow_string_concat))
print(timeit.timeit(test_fast_string_concat))


def mutable_add_element(element, elements=[]):
    elements.append(element)
    return elements

def add_element(element, elements=None):
    if not elements:
        elements = []
    elements.append(element)
    return elements
