import logging


def setup_logger(level: int = logging.INFO, fname: str = __name__) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)s | %(name)s: %(message)s",
        datefmt="[%H:%M:%S]",
        level=level,
        handlers=[logging.FileHandler(f"log/{fname}.log", mode='w'), ],
    )
