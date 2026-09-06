# purchase-toolkit-ops

Scripts que utilizan la librería [`purchase-toolkit`](https://github.com/ochoaenzo/purchase-toolkit) para automatizar el circuito de órdenes de compra.

## Requisitos

- Python 3.14
- [`uv`](https://docs.astral.sh/uv/)

## Instalación

```bash
uv sync
```

## Configuración

Copiar `config.example.toml` a `config.toml` y completar las rutas locales.

## Uso

```bash
uv run merge.py
```

Agrupa los PDF de órdenes de compra pendientes de enviar a firma en un único archivo por orden, usando `purchase_toolkit.merge.PurchaseOrderPdfMerger`.
