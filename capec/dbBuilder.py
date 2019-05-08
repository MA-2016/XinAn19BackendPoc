# abondoned fields:
#   Attack_Patterns/AttackPattern/Mitigations
#   Attack_Patterns/AttackPattern/Example_Instance
#   Attack_Patterns/AttackPattern/Content_History
#   Attack_Patterns/AttackPattern/Taxonomy_Mapping
#   Attack_Patterns/AttackPattern/Prerequisites
#   Attack_Patterns/AttackPattern/Skills_Required
#   Attack_Patterns/AttackPattern/Consequences
#   Attack_Patterns/AttackPattern/Resources_Required
#   Attack_Patterns/Execution_Flow/Attack_Step/Technique
#
# questions:
#   what's taxonomy mapping (分类匹配) for?
# note:


import xmltodict
import collections
import json
from py2neo import Graph, Node, Relationship

# open data file
with open('ComprehensiveCAPECDictionary.xml', 'rb') as f:
    data = xmltodict.parse(f.read().decode('utf8'))
    root = data['Attack_Pattern_Catalog']

graph = Graph('http://localhost:7474', username='neo4j', password='Luncert428')

# help function

def is_list(obj):
    return isinstance(obj, list)

def adapt_list(item):
    return [i for i in item if not i is None] if is_list(item) else [item]

def sub_SkillsRequired(item):
    ret = []
    for i in adapt_list(item):
        obj = {}
        if '@Level' in i: obj['level'] = i['@Level']
        if '#text' in i: obj['skill'] = i['#text']
        ret.append(obj)
    return ret

def sub_Consequences(item):
    return [{'scopes': adapt_list(i['Scope']), 'impact': i['Impact']} for i in adapt_list(item)]

def handle_AttackPatterns():
    relatedAps = {}
    for ap in root['Attack_Patterns']['Attack_Pattern']:
        apNode = Node('AttackPattern')
        if '@ID' in ap: apNode['capecID'] = int(ap['@ID'])
        if '@Name' in ap: apNode['name'] = ap['@Name']
        if '@Abstraction' in ap: apNode['abstraction'] = ap['@Abstraction']
        if '@Status' in ap: apNode['status'] = ap['@Status']
        if '@Description' in ap: apNode['description'] = ap['@Description']
        if 'Likelihood_Of_Attack' in ap: apNode['likelihoodOfAttack'] = ap['Likelihood_Of_Attack']
        if 'Typical_Severity' in ap: apNode['typicalSeverity'] = ap['Typical_Severity']
        # if 'Prerequisites' in ap: apNode['prerequisites'] = json.dumps(adapt_list(ap['Prerequisites']['Prerequisite']))
        # if 'Skills_Required' in ap: apNode['skillsRequired'] = json.dumps(sub_SkillsRequired(ap['Skills_Required']['Skill']))
        # if 'Consequences' in ap: apNode['consequences'] = json.dumps(sub_Consequences(ap['Consequences']['Consequence']))
        # if 'Resources_Required' in ap: apNode['resourcesRequired'] = json.dumps(adapt_list(ap['Resources_Required']['Resource']))
        graph.create(apNode)

        # handle Execution_Flow
        if 'Execution_Flow' in ap:
            efNodes = []
            for ef in adapt_list(ap['Execution_Flow']['Attack_Step']):
                efNode = Node('AttackStep')
                if 'Step' in ef: efNode['stepOrder'] = int(ef['Step'])
                if 'Phase' in ef: efNode['phase'] = ef['Phase']
                if 'Description' in ef:
                    desc = ef['Description']
                    if isinstance(desc, str): efNode['description'] = desc
                    else:
                        s = ''
                        for tagName, content in desc.items():
                            tagName = tagName[tagName.find(':') + 1:]
                            s += '<%s>%s</%s>' % (tagName, content, tagName)
                        efNode['description'] = s
                # if 'Technique' in ef: efNode['techniques'] = json.dumps(adapt_list(ef['Technique']))
                efNodes.append(efNode)
            if len(efNodes) > 0:
                efNodes = sorted(efNodes, key=lambda efNode: efNode['stepOrder'])
                # associate the first efNode with apNode
                graph.create(Relationship(apNode, 'Own', efNodes[0]))
                for i in range(1, len(efNodes)):
                    efNode = efNodes[i]
                    graph.create(Relationship(efNodes[i - 1], 'Precede', efNode))
                    graph.create(Relationship(apNode, 'Own', efNode))
        
        # save Related_Attack_Patterns
        if 'Related_Attack_Patterns' in ap:
            relatedAps[apNode['capecID']] = [{'nature': rap['@Nature'], 'capecID': int(rap['@CAPEC_ID'])}
                for rap in adapt_list(ap['Related_Attack_Patterns']['Related_Attack_Pattern'])]
    
    for cid, raps in relatedAps.items():
        n1 = graph.nodes.match('AttackPattern', capecID=cid).first()
        for rap in raps:
            n2 = graph.nodes.match('AttackPattern', capecID=rap['capecID']).first()
            graph.create(Relationship(n1, rap['nature'], n2))

def handle_Categories():
    rs = {}
    for c in root['Categories']['Category']:
        cNode = Node('Category')
        if '@ID' in c: cNode['capecID'] = int(c['@ID'])
        if '@Name' in c: cNode['name'] = c['@Name']
        if 'Summary' in c: cNode['summary'] = c['Summary']
        graph.create(cNode)

        # handle relationships
        if 'Relationships' in c:
            rs[cNode['capecID']] = [int(r['@CAPEC_ID']) for r in adapt_list(c['Relationships']['Has_Member'])]
    
    for cid, r in rs.items():
        base = graph.nodes.match(capecID=cid).first()
        for i in r:
            target = graph.nodes.match(capecID=i).first()
            graph.create(Relationship(base, 'HasMember', target))

if __name__ == "__main__":
    # handle_AttackPatterns()
    handle_Categories()