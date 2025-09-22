import memutil
from doomed import Doomed
import gc


def main():
    print()
    ref_counting()
    print()
    print()
    gcing()
    print('PROGRAM ENDING!', flush=True)


def ref_counting():
    gc.disable()

    v1 = Doomed()
    v1_id = id(v1)

    print(f'Step 1: Ref count is {memutil.refs(v1_id)}')

    v2 = v1
    print(f'Step 2: Ref count is {memutil.refs(v1_id)}')

    v2 = None  # noqa: F841
    print(f'Step 3: Ref count is {memutil.refs(v1_id)}')

    v1 = None
    print(f'Step 4: Ref count is {memutil.refs(v1_id)}')

    print('End of method!', flush=True)


def gcing():
    gc.enable()

    v1 = Doomed()
    v2 = Doomed(v1)
    v1.friends.append(v2)

    v1_id = id(v1)
    v2_id = id(v2)

    print(f'Step 1: GC count is {memutil.refs(v1_id)} {memutil.refs(v2_id)}')

    v1 = None
    v2 = None
    print(f'Step 2: GC count is {memutil.refs(v1_id)} {memutil.refs(v2_id)}')

    gc.collect()
    print(f'Step 3: GC count is {memutil.refs(v1_id)} {memutil.refs(v2_id)}')

    print('End of method!', flush=True)


if __name__ == '__main__':
    main()
