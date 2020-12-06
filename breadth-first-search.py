gr = {'start': {'car':{'bar':{'bat': None}}, 'cat':{'mat': {'bat': None}, 'bat': None}, 'can': {'ban':{'bun': {'bat': None}, 'bat2':{'1':{'2': None}} }}}}

def rec2(gr, counter):
    if None in gr.values():
        return counter + 1, [k for k, v in gr.items() if v is None]

    cnt_min = 0
    for k, v in gr.items():
        cnt, keys = rec2(v, counter)
        if not cnt_min or cnt < cnt_min:
            cnt_min = cnt
            min_path = [k]
            min_path.extend(keys)

    counter += cnt_min
    return counter, min_path

def find_traces(gr):
    traces = []

    for k,v in gr['start'].items():
        counter, min_path = rec2(v, 1)
        path = [k]
        path.extend(min_path)
        traces.append((path, counter))

    return sorted(traces).pop()
