"""Agrupa los PDF de órdenes de compra pendientes de enviar a firma."""

import logging
from pathlib import Path

from purchase_toolkit.merge.purchase_orders_pdf import PurchaseOrderPdfMerger

from config import load_config


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.getLogger("pypdf").setLevel(logging.ERROR)

    config = load_config()["merge"]
    source_folder = Path(config["source_folder"])
    destination_folder = Path(config["destination_folder"])

    merger = PurchaseOrderPdfMerger()
    merger.merge(source_folder, destination_folder)


if __name__ == "__main__":
    main()
