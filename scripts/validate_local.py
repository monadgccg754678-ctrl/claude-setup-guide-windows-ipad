from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
files=json.loads((root/'manifest.json').read_text(encoding='utf-8'))['files']
for rel,expected in files.items():
 p=(root/rel).resolve()
 assert p.is_relative_to(root.resolve()) and p.is_file(),rel
 assert not set(Path(rel).parts)&{'.local','.git','connection-private'},rel
 assert hashlib.sha256(p.read_bytes()).hexdigest()==expected,rel
for rel in ['SKILL.md','references/16-windows-ipad-apple-practice.md']:
 for target in re.findall(r'\]\(([^)]+)\)',(root/rel).read_text(encoding='utf-8')):
  if '://' in target or target.startswith('#') or target=='图片的实际绝对路径':continue
  assert (root/rel).parent.joinpath(target.split('#')[0]).exists(),target
print('PASS:',len(files),'files; integrity, private paths and supplement links')
