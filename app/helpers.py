def list_to_tree(data, rootid):
    out = { 
        rootid: { 'id': 0, 'parent_id': 0, 'name': "root", 'children': [] }
    }
    for p in data:
        out.setdefault(p['parent_id'], { 'children': [] })
        out.setdefault(p['id'], { 'children': [] })
        out[p['id']].update(p)
        out[p['parent_id']]['children'].append(out[p['id']])
    return out[rootid] 