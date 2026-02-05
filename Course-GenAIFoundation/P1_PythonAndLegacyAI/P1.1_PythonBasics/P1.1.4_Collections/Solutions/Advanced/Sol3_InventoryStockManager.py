"""
Advanced Solution 3: Inventory Stock Manager
"""

# Input data
dependencies_data = """Laptop:CPU,RAM,SSD,Screen
Desktop:CPU,RAM,HDD,GPU
Server:CPU,RAM,HDD,NetworkCard
Tablet:CPU,RAM,Screen,Battery"""

# Build dependency graph
graph = {}
all_components = set()

for line in dependencies_data.split('\n'):
    product, components_str = line.split(':')
    components = {c.strip() for c in components_str.split(',')}
    graph[product] = components
    all_components.update(components)

# Find shared components (used by multiple products)
component_usage = {}
for product, components in graph.items():
    for comp in components:
        if comp not in component_usage:
            component_usage[comp] = set()
        component_usage[comp].add(product)

shared_components = {comp: products for comp, products in component_usage.items() if len(products) > 1}

# Products with no dependencies (this example has none, but showing the logic)
products_no_deps = [p for p, deps in graph.items() if len(deps) == 0]

# Show dependency chain
print("Product Dependencies:")
for product, components in graph.items():
    print(f"{product}: {components}")

print("\nShared Components (used by multiple products):")
for comp, products in shared_components.items():
    print(f"{comp}: {products}")

print("\nComponent Usage Summary:")
for comp in sorted(all_components):
    count = len(component_usage[comp])
    print(f"{comp}: used by {count} products")
