# Repository Abstraction for SharePoint Services

> **Module 08: SharePoint Operations | Topic 04**

## 1. Learning Outcomes
- **Decoupled Architecture:** Wrap SharePoint REST operations behind abstract domain interfaces.
- **Pluggable Storage:** Swap between local SQLite and remote SharePoint repositories seamlessly.
- **Domain Mapping:** Transform SharePoint JSON dictionaries into clean domain dataclasses.
- **Testability:** Enable test execution without depending on active Microsoft 365 environments.

## 2. Key Architecture Pattern

```python
from abc import ABC, abstractmethod
from typing import List

class IAssetRepository(ABC):
    @abstractmethod
    def add_asset(self, asset: dict) -> None:
        pass

    @abstractmethod
    def list_assets(self) -> List[dict]:
        pass

# Production Implementation: Connects to SharePoint
class SharePointAssetRepository(IAssetRepository):
    def __init__(self, sp_client):
        self.client = sp_client

    def add_asset(self, asset: dict) -> None:
        self.client.create_item({"Title": asset["name"], "Value": asset["value"]})

    def list_assets(self) -> List[dict]:
        items = self.client.get_items()
        return [{"name": item["Title"], "value": item["Value"]} for item in items]

# Test Implementation: In-Memory (Zero cloud dependencies)
class InMemoryAssetRepository(IAssetRepository):
    def __init__(self):
        self.items = []

    def add_asset(self, asset: dict) -> None:
        self.items.append(asset)

    def list_assets(self) -> List[dict]:
        return list(self.items)
```

## 3. Common Mistakes & Gotchas
- **Leaking SharePoint Types:** Letting SharePoint XML/JSON schema leak into user interface layers couples UI directly to Microsoft APIs.
- **Missing Error Translation:** Wrap `HTTPError` in custom domain exceptions like `RepositoryConnectionError`.

## 4. Practice Tasks
- **Task 1:** Create an interface `IDocumentStore` and implement a local file-system version and a SharePoint stub.

## 5. Self-Check Questions
- **Q1:** Why is repository abstraction crucial when building SharePoint-backed applications?
- **Q2:** How does abstraction help automated testing in CI/CD pipelines?
