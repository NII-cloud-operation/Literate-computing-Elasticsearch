# coding: utf-8

from IPython.display import display
import ipywidgets as widgets
import codecs

ITEM1 = u'お試し用構成 1TB'
ITEM2 = u'運用可能最小構成 1.5TB'
ITEM3 = u'運用可能高性能構成 2.5TB'

struct_dropdown = widgets.Dropdown(options=[u'選択してください',ITEM1,ITEM2,ITEM3], value=u'選択してください')
button = widgets.Button(description=u"設定ファイル出力")

def show_selector(cluster_name):
	global CLUSTER_NAME
	CLUSTER_NAME = cluster_name

	struct_dropdown.observe(on_value_change, names='value')
	
	button.disabled = True
	button.on_click(on_button_clicked)
	display(struct_dropdown, button)

def on_value_change(change):
    button.disabled = (change['new'] == u'選択してください')

def get_hosts(start, end):
    ret = ''
    for idx in range(start, end+1) :
         ret = ret + '{{host{0}}}\n'.format(idx)
    return ret

def on_button_clicked(b):
    global CLUSTER_NAME

    SPECS_TEMPLATE = u"ホスト数: {0}\nCPU数: {1}\nメモリ(GB): {2}\nディスクサイズ(GB): {3}\n"
    HOSTS_TEMPLATE = u"[all]\n{0}\n[master-nodes]\n{1}\n[data-nodes]\n{2}\n[ingest-nodes]\n{3}\n[logstash-server]\n{4}"
    GROUP_VARS_TEMPLATE = u"cluster_name: {0} #クラスタ名\nshards: {1} #Shard数\nreplicas: {2} #Replica数\nmin_master_nodes: {3} #最小Master Node数\nes_heap_size: {4} #ヒープサイズ\n"
    struct = struct_dropdown.value
    if(struct == ITEM1) :
        specs= SPECS_TEMPLATE.format(1, 8, 64, 1024)
        inventory = HOSTS_TEMPLATE.format(get_hosts(1,1), get_hosts(1,1), get_hosts(1,1), get_hosts(1,1), "")
        params = GROUP_VARS_TEMPLATE.format(CLUSTER_NAME, 1, 0, 1, '31g')
    elif(struct == ITEM2):
        specs= SPECS_TEMPLATE.format(3, 8, 64, 3072)
        inventory = HOSTS_TEMPLATE.format(get_hosts(1,3), get_hosts(1,3), get_hosts(1,3), get_hosts(1,3), get_hosts(1,1))
        params = GROUP_VARS_TEMPLATE.format(CLUSTER_NAME, 3, 1, 2, '31g')
    elif(struct == ITEM3):
        specs= SPECS_TEMPLATE.format(5, 8, 64, 5120)
        inventory = HOSTS_TEMPLATE.format(get_hosts(1,5), get_hosts(1,3), get_hosts(1,5), get_hosts(1,5), get_hosts(4,4))
        params = GROUP_VARS_TEMPLATE.format(CLUSTER_NAME, 5, 1, 3, '31g')
        
    print(u"●「" + struct_dropdown.value + u"」構成を出力")
    with codecs.open("./hosts_template", "w", 'utf-8') as f:
        f.write(inventory)
        f.close()
    print("====================================")
    print("インベントリ → ./hosts_template に出力")
    print("------------------------------------")
    print(inventory)
    with codecs.open("./group_vars/all", "w", 'utf-8') as f:
        f.write(params)
        f.close()
    print("====================================")
    print("パラメータ → ./group_vars/allに出力")
    print("------------------------------------")
    print(params)
    print("====================================")
    print("★以下の収容パラメータは、")
    print("01_02_Accommodation_XXX.ipynbのNotebook")
    print("にて手で入力してください")
    print("------------------------------------")
    print(specs)
