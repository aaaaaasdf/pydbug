import runpy


class PyException:
    def __init__(self, info):
        self.info = info
    def __repr__(self):
        return f"{self.info[0]}: {self.info[1]}"


def run(path):
    try:
        runpy.run_path(path, init_globals=None, run_name="__main__")
        return 1
    except Exception as e:
            return PyException(
                (
                    type(e),
                    str(e)
                )
            )

