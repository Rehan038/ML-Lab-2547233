import json
from pathlib import Path
p = Path('ML-LAB1/ML_LAB1.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
changed = False
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        src = '\n'.join(cell.get('source', []))
        new = src
        # Fix label f-strings that use single quotes outside
        new = new.replace("label=f'Most Polluted (", 'label=f"Most Polluted (')
        new = new.replace("label=f'Least Polluted (", 'label=f"Least Polluted (')
        # Fix plt.text inner f-strings
        new = new.replace("f'{most_polluted_year['AQI']:.2f}'", 'f"{most_polluted_year[\'AQI\']:.2f}"')
        new = new.replace("f'{least_polluted_year['AQI']:.2f}'", 'f"{least_polluted_year[\'AQI\']:.2f}"')
        # Also handle general pattern: f'{var['key']:.2f}' -> f"{var['key']:.2f}"
        # A simple safe replace for common patterns
        new = new.replace("f'{most_polluted_year['", 'f"{most_polluted_year[')
        new = new.replace("f'{least_polluted_year['", 'f"{least_polluted_year[')
        if new != src:
            cell['source'] = [line + '\n' for line in new.split('\n')]
            changed = True
if changed:
    p.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding='utf-8')
    print('Notebook updated')
else:
    print('No changes needed')
