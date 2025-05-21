def _helper():
    print("This is a private helper function.")

def public():
    print("This is a public function.")

__all__ = ["public"]