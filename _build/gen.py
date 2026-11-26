# 사이트 생성기: python3 _build/gen.py  (공통 메뉴, 푸터, 다음으로 블록을 한 곳에서 관리)
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME = 'https://sei-ban.github.io/memory-ender/?v=1124'

PROJECTS = [
  dict(slug='memory-ender', tag='PROJECT 01 | 개인 프로젝트, 웹 게임', name='메모리 엔더',
       hook='기억을 지우는 장의사가 장례를 거부한 망자를 쫓아, 마지막 장례를 치른다. 쌓아 온 감정을 마지막에 플레이어의 손으로 터뜨리는 구조.',
       thumb='assets/img/me-climax.jpg'),
  dict(slug='aftermath', tag='PROJECT 02 | 5인 팀, Unity', name='Aftermath',
       hook='3인 온라인 협동 타워 디펜스. 컨셉 원안을 내고 콘텐츠 기획을 맡아, 기획서와 데이터테이블, 요청서로 구현까지 연결했다.',
       thumb='assets/img/af-battle-full.jpg', color='#2F5496'),
  dict(slug='echo', tag='PROJECT 03 | 개인 프로젝트, Unity 6', name='잔향 (Echo)',
       hook='"10초 전의 내가 지금의 동료가 된다", 수치로 정답 루트를 고정한 시간 루프 퍼즐 플랫포머.',
       thumb='assets/img/echo-tower.jpg', color='#3A4F7A'),
  dict(slug='whoami', tag='PROJECT 04 | 5인 팀, 비주얼 노벨', name='WHO AM I?',
       hook='감정 순서대로 여섯 방을 배치한 추리 비주얼 노벨.',
       thumb='assets/img/who-lobby.jpg', color='#4A5D85'),
]

ANALYSES = [
  dict(href='analysis.html', tag='ANALYSIS 01 | 수집형 RPG', name='트릭컬 리바이브', hook='분석 문서 준비 중입니다.', color='#2F5496'),
]

def acard(a, p):
    return f'''<a class="card" href="{p}{a["href"]}"><div class="thumb"><div class="txt" style="background:{a["color"]}">{a["name"]}</div></div><div class="c"><div class="tag">{a["tag"]}</div><h4>{a["name"]}</h4><p>{a["hook"]}</p><div class="more">자세히 보기</div></div></a>'''

def head(title, depth, active):
    p = '../' * depth
    nav = [('index.html#projects', '기획 프로젝트', 'home'), ('index.html#analysis', '게임 분석 및 제안', 'analysis'), ('about.html', '소개', 'about')]
    items = ''.join(f'<li><a href="{p}{h}" class="{"on" if k == active else ""}" data-nav="{k}">{t}</a></li>' for h, t, k in nav)
    return f'''<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="콘텐츠, 시스템 기획자 김준현 포트폴리오">
<link rel="stylesheet" href="{p}assets/style.css?v=12"></head><body>
<nav class="top"><div class="wrap"><a class="brand" href="{p}index.html">김준현<span>게임 기획 포트폴리오</span></a><ul>{items}</ul></div></nav>
'''

def foot(depth):
    p = '../' * depth
    return f'''<footer><div class="wrap"><span>김준현, junhyeon.kim.work@gmail.com</span><span><a href="{GAME}" target="_blank" rel="noopener">메모리 엔더 플레이</a></span></div></footer>
<script src="{p}assets/site.js?v=7"></script></body></html>'''

def card(pr, p):
    if pr['thumb']:
        th = f'<img src="{p}{pr["thumb"]}" alt="">'
    else:
        nudge = 'padding-right:28px;' if pr['name'].endswith('?') else ''
        th = f'<div class="txt" style="background:{pr["color"]};{nudge}">{pr["name"]}</div>'
    return f'''<a class="card" href="{p}projects/{pr["slug"]}.html"><div class="thumb">{th}</div><div class="c"><div class="tag">{pr["tag"]}</div><h4>{pr["name"]}</h4><p>{pr["hook"]}</p><div class="more">자세히 보기</div></div></a>'''

CYCLE = [(x['slug'], 'projects/' + x['slug'] + '.html', x['name'], x['hook'], 'NEXT PROJECT') for x in PROJECTS] + \
        [('analysis', 'analysis.html', '게임 분석 및 제안', '상용 게임이 감정을 쌓고 터뜨리는 구조를 분석하고 개선안을 제안', 'NEXT')]

def next_block(slug, depth=1):
    p = '../' * depth
    i = [x[0] for x in CYCLE].index(slug)
    nx = CYCLE[(i + 1) % len(CYCLE)]
    hook = nx[3] if len(nx[3]) <= 48 else nx[3][:48] + '…'
    return f'''<section class="next"><div class="wrap"><div class="grid">
<a class="box dark" href="{p}about.html"><small>ABOUT</small><b>이 기획을 한 사람</b><span>연출에서 게임 기획으로, 일하는 방식</span></a>
<a class="box" href="{p}{nx[1]}"><small>{nx[4]}</small><b>{nx[2]}</b><span>{hook}</span></a>
</div></div></section>'''

def write(path, html):
    if path.startswith('projects/') and '</header>' in html:
        slug = os.path.basename(path)[:-5]
        html = html.replace('</header>', '</header>' + next_block(slug).replace('class="next"', 'class="next top"'), 1)
        html = html.replace('<footer', next_block(slug) + '<footer', 1)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(html)

# ---------------- 홈 ----------------
home = head('김준현 | 게임 기획 포트폴리오', 0, 'home') + f'''
<header class="hero"><div class="wrap">
<div class="k">GAME DESIGNER | 신입</div>
<h1>오래 남는 순간은 우연이 아니라 설계입니다.</h1>
<p class="lead">오래 기억될 한순간, 그 순간까지의 감정과 규칙, 수치를 설계하는 콘텐츠, 시스템 기획자 김준현입니다.</p>
<div class="video" data-v="memory-ender"><div class="ph"><img src="assets/img/me-chase.jpg" alt=""><div><b style="font-size:20px;color:#fff">메모리 엔더 플레이 영상</b><br>영상 준비 중. 아래 버튼으로 바로 플레이할 수 있습니다</div></div></div>
<div class="btns"><a class="btn p" href="{GAME}" target="_blank" rel="noopener">메모리 엔더 바로 플레이 (약 5분)</a><a class="btn g" href="projects/memory-ender.html">기획 의도 보기</a></div>
</div></header>
<section class="s slider-sec"><div class="wrap">
<div class="sl-tabs" role="tablist"><button class="sl-tab on" data-i="0" role="tab">기획 프로젝트</button><button class="sl-tab" data-i="1" role="tab">게임 분석 및 제안</button></div>
<div class="slider">
<button class="sl-arrow sl-prev" aria-label="이전 칸" data-d="-1"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button>
<div class="sl-view"><div class="sl-track">
<div class="sl-panel"><p class="st">카드를 누르면 기획 의도와 설계, 작업 내역을 볼 수 있습니다.</p>
<div class="cards">{''.join(card(pr, '') for pr in PROJECTS)}</div></div>
<div class="sl-panel"><p class="st">상용 게임이 감정을 어디서 쌓고 어디서 터뜨리는지 뜯어 보고, 개선안과 새 콘텐츠를 제안합니다. 카드를 누르면 분석과 제안 문서를 볼 수 있습니다.</p>
<div class="cards">{''.join(acard(a, '') for a in ANALYSES)}</div></div>
</div></div>
<button class="sl-arrow sl-next" aria-label="다음 칸" data-d="1"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></button>
</div>
</div></section>
<section class="next"><div class="wrap"><div class="grid">
<a class="box dark" href="about.html"><small>ABOUT</small><b>이 프로젝트들을 만든 사람</b><span>연출 전공에서 게임 기획으로 온 이야기와 일하는 방식</span></a>
<a class="box" href="analysis.html"><small>GAME ANALYSIS &amp; PROPOSAL</small><b>게임 분석 및 제안</b><span>상용 게임의 감정 구조를 분석하고 개선안을 제안</span></a>
</div></div></section>
''' + foot(0)
write('index.html', home)

# ---------------- 메모리 엔더 ----------------
me = head('메모리 엔더 | 김준현', 1, 'home') + f'''
<header class="phead"><div class="wrap"><div class="k">PROJECT 01 | 개인 프로젝트, 웹 게임</div><h1>메모리 엔더 (Memory Ender)</h1><p>기억을 지우는 장의사가 장례를 거부한 망자를 쫓아, 마지막 장례를 치른다</p></div></header>
<section class="s" style="padding-top:28px"><div class="wrap">
<div class="video" data-v="memory-ender"><div class="ph"><img src="../assets/img/me-funeral.jpg" alt=""><div><b style="font-size:20px;color:#fff">플레이 영상</b><br>영상 준비 중</div></div></div>
<div class="btns"><a class="btn n" href="{GAME}" target="_blank" rel="noopener">바로 플레이 (설치 없이 브라우저, 약 5분)</a><a class="btn o" href="../files/memory-ender-gdd.pdf">게임 기획서 PDF</a><a class="btn o" href="https://github.com/sei-ban/memory-ender">저장소</a></div>
<p class="note" style="margin-top:8px">타이틀의 챕터 선택으로 원하는 구간을 바로 볼 수 있습니다. 클라이맥스는 '3. 장례'.</p>
<div class="stats"><div class="stat"><b>3구간</b><span>추리, 추격, 장례</span></div><div class="stat"><b>35</b><span>플레이 튜닝 항목</span></div><div class="stat"><b>약 5분</b><span>첫 에피소드</span></div><div class="stat"><b>9초</b><span>클라이맥스, 직접 누르는 시간</span></div></div>
<table class="info"><tr><td class="h">기간</td><td>2026.11.19 ~ 24 (6일): 기획, 구현, 아트, 웹 배포</td></tr><tr><td class="h">역할</td><td>1인. 기획, 감정 설계, 튜닝 결정 (구현은 Claude 협업)</td></tr><tr><td class="h">장르</td><td>스토리 중심 액션 어드벤처 (현재 빌드는 망자 한 명의 첫 에피소드, 이후 에피소드로 확장)</td></tr><tr><td class="h">사용 툴</td><td>Claude, Claude Code, Git, GitHub Pages</td></tr></table>
<div class="gallery"><img src="../assets/img/me-title.jpg" alt="타이틀"><img src="../assets/img/me-investigate.jpg" alt="추리"><img src="../assets/img/me-chase.jpg" alt="추격"><img src="../assets/img/me-funeral.jpg" alt="장례"><img src="../assets/img/me-memory.jpg" alt="기억 장면"><img src="../assets/img/me-climax.jpg" alt="클라이맥스"></div>
<p class="cap">타이틀, 추리, 추격, 장례, 기억 장면, 클라이맥스. 외부 이미지 없이 코드로 그린 도트 그림이고, 사운드는 브라우저에서 직접 합성했다.</p>

<h3>기획 의도</h3>
<p>빌드업을 쌓아 클라이맥스에서 터지는 한순간이 핵심 재미이며, 그 순간이 플레이를 계속하게 만든다. 중심 감정은 <b>연민과 갈등</b>이다. 지워야 한다는 걸 알지만 지우고 싶지 않은 마음을, 플레이어가 마지막에 <b>자기 손으로</b> 결정하게 만든다.</p>

<h3>목표 감정 곡선</h3>
<div class="fig"><img src="../assets/img/emotion_curve.png" alt="감정 곡선"></div>
<p class="cap">실측값이 아닌 설계 목표. 추격 끝에서 긴장감은 내려가고, 장례로 넘어가며 연민, 갈등이 정점까지 올라간다.</p>

<h3>빌드업 구조: 구간마다 쌓는 감정과 장치</h3>
<table><tr><th style="width:14%">구간</th><th style="width:20%">쌓이는 감정</th><th>기대 장치</th><th>방해 장치</th></tr>
<tr><td><b>추리</b></td><td>사명감에서 관계 추측으로</td><td>단서 3개로 관계가 조금씩 드러남 (결과, 장소, 동기 순)</td><td>신호로만 위치를 앎, 오답이면 다시 추리</td></tr>
<tr><td><b>추격</b></td><td>긴박감 + 연민의 시작</td><td>망자를 맞힐 때마다 기억 문장(주마등) 공개. 웃던 밤에서 싸우기 직전의 밤 순서</td><td>망자 회피 3종, 붕괴 지형, 잔해</td></tr>
<tr><td><b>장례</b></td><td>갈등</td><td>갑옷 파츠를 뜯을 때마다 둘의 기억 장면으로 전환</td><td>끌어당기는 저항감, 순서 고정</td></tr>
<tr><td><b>클라이맥스</b></td><td>연민과 갈등의 정점</td><td>데이터 망자를 누르는 동안 마지막 독백 진행</td><td>손을 떼면 멈춤. 끝낼지는 플레이어가 쥐고 있음</td></tr></table>

<h3>핵심 플레이: 추격 코어 루프</h3>
<div class="fig"><img src="../assets/img/core_loop.png" alt="코어 루프"></div>

<h3>클라이맥스 설계</h3>
<p>갑옷 5개를 모두 뜯어내면 데이터 망자만 남는다. 조등(장의사의 장례 도구)을 대고 <b>누르고 있는 9초</b> 동안 마지막 독백 3줄이 흐르고, 손을 떼면 멈춘다. 마지막 줄 "다음 편은… 혼자 봐야 할 거 같아."는 추격의 주마등 "다음 편은 내일 같이 보자."를 회수한다. 이후 현실의 방에서 그녀는 혼자 소파에 앉아, 이유 모를 허전함을 느낀다.</p>

<h3>문제, 판단, 해결 (튜닝 기록 35항목 중)</h3>
<table><tr><th style="width:28%">문제 (플레이하며 느낀 점)</th><th style="width:30%">판단</th><th>해결</th></tr>
<tr><td>장례가 단순 홀드라 아무 감정도 전달되지 않음</td><td>지우는 행위 자체가 감정을 만들어야 한다</td><td>기사의 갑옷 파츠를 정해진 순서로 <b>직접 붙잡고 뜯어내는 조작</b>으로 재설계</td></tr>
<tr><td>포착 링 2초가 늘어져 긴박감이 없음</td><td>추격의 리듬을 해치는 늘어짐 제거</td><td>링 2초를 <b>1초</b>로, 흡수는 홀드에서 <b>3초 안에 연타 10회</b>로</td></tr>
<tr><td>가시, 함정, 공격이 겹쳐 무조건 맞는 순간</td><td>불합리하게 지면 쌓아 온 몰입이 깨진다</td><td>기믹이 겹치지 않게 배치, 회피 전 <b>0.4초 예고</b></td></tr>
<tr><td>문구만으로는 둘에게 무슨 일이 있었는지 와닿지 않음</td><td>보여 주는 것이 읽히는 것보다 강하다</td><td>파츠를 뜯을 때마다 <b>기억 장면으로 화면 전환</b> (5초)</td></tr>
<tr><td>주마등 문장이 흡수 완료 시점에 나옴</td><td>망자가 맞은 타이밍에 나와야 한다</td><td>공개 시점을 <b>명중 순간</b>으로 이동 (2.6초)</td></tr></table>
<p class="note">전체 35항목은 게임 기획서 7-5~7-7에 변경 전, 후 수치와 이유를 함께 기록했다.</p>

<h3>한순간을 지키기 위해 바꾼 것</h3>
<p>장례는 처음에 버튼을 누르고 있는 단순 홀드였다. 지우는 행위 자체가 감정을 만들어야 한다고 판단해, 갑옷 파츠를 정해진 순서로 직접 뜯어내는 조작으로 다시 설계했다. 마지막 9초의 누르기는 끝낼지를 플레이어가 쥐고 있게 하는 장치라 끝까지 남겼다.</p>
<div class="lesson"><b>배운 점</b>한순간은 그 장면만 잘 만든다고 터지지 않았다. 앞에서 쌓인 감정이 있어야 같은 9초가 무거워졌고, 그래서 늘어짐과 불합리한 순간을 걷어 내는 튜닝이 클라이맥스를 만드는 일만큼 중요했다.</div>
</div></section>
''' + foot(1)
write('projects/memory-ender.html', me)

# ---------------- Aftermath ----------------
af = head('Aftermath | 김준현', 1, 'home') + '''
<header class="phead"><div class="wrap"><div class="k">PROJECT 02 | 팀 프로젝트, Unity</div><h1>Aftermath</h1><p>3인 온라인 협동 타워 디펜스 (2026.09 ~ 12). 게임 컨셉 원안을 냈다 (컨셉 원페이저, 원안 김준현, 편집 팀원).</p></div></header>
<section class="s" style="padding-top:28px"><div class="wrap">

  <div class="stats"><div class="stat"><b>40+</b><span>작성한 기획 문서</span></div><div class="stat"><b>73</b><span>규칙 변경 요청, 명세 반영</span></div><div class="stat"><b>37</b><span>Jira 담당 이슈</span></div><div class="stat"><b>10</b><span>1차 빌드 구현 PR</span></div></div>
  <table class="info"><tr><td class="h">기간</td><td>2026.09 ~ 12 (12.04 발표회)</td><td class="h">역할</td><td>컨셉 원안, 콘텐츠 기획 (5인 팀)</td></tr><tr><td class="h">장르</td><td>3인 온라인 협동 타워 디펜스 (PC)</td><td class="h">사용 툴</td><td>Unity, Jira, Confluence, Git, Claude</td></tr></table>
  <div class="gallery"><img src="../assets/img/af-title.jpg" alt="타이틀"><img src="../assets/img/af-day-full.jpg" alt="낮 준비"><img src="../assets/img/af-battle-full.jpg" alt="밤 전투"><img src="../assets/img/af-skill-full.jpg" alt="스킬트리"><img src="../assets/img/af-estate-full.jpg" alt="국왕 영지"><img src="../assets/img/af-diplo-full.jpg" alt="귀족 외교"></div>
  <p class="cap">타이틀, 낮 준비, 밤 전투, 스킬트리, 국왕 영지, 귀족 외교. 개발 빌드 화면이며 아트와 구현은 팀 공동 작업이다.</p>
  <h3>담당한 콘텐츠</h3>
  <table><tr><th style="width:21%">콘텐츠</th><th style="width:47%">한 일</th><th>숫자</th></tr>
   <tr><td>스킬트리</td><td>스킬 상세 기획, 데이터테이블을 구현값에 맞춰 정리, 단일 대상 스킬을 범위형으로 보완</td><td>데이터테이블 v7, 담당별 요청 11건</td></tr>
   <tr><td>튜토리얼</td><td>단계 흐름 기획과 화면 와이어프레임, 이후 캠페인 방식으로 전환</td><td>7단계</td></tr>
   <tr><td>국왕, 기사, 귀족 추가 콘텐츠</td><td>직업별 세부기획서, 데이터테이블, UI 요구서</td><td>국왕 데이터테이블 v8</td></tr>
   <tr><td>장비 시스템</td><td>슬롯, 일반 장비와 특수 장비, 부여 규칙, 아트 요청</td><td>일반 6종, 특수 24종, 아이콘 36종</td></tr>
   <tr><td>국왕 자동화</td><td>영지 단계와 생산 체인 자동화, 가공 대기열 조정</td><td>영지 4단계, 대기열 5칸에서 10칸</td></tr>
   <tr><td>귀족 정책 카드</td><td>낮 이벤트를 완수해 카드를 받고 발동하는 영지 안 콘텐츠 (아래 사례 1)</td><td>카드 21장, 계열 3개</td></tr>
   <tr><td>프롤로그 캠페인</td><td>6장 전체 흐름과 장별 세부기획 (아래 사례 2)</td><td>6장, 계산 58.4분</td></tr></table>
  <h3>구현 담당이 바로 작업할 수 있는 전달 방식</h3>
  <table><tr><th style="width:22%">단계</th><th>내용</th></tr>
   <tr><td>기획서</td><td>규칙, 예외, 수치의 의도를 먼저 쓰고 상세는 표로</td></tr>
   <tr><td>데이터테이블</td><td>수치의 원본. 기획서보다 우선하도록 버전 관리</td></tr>
   <tr><td>구현, UI, 아트 요청서</td><td>받는 사람별로 나눠 무엇을, 왜, 어떤 우선순위로 할지만 전달. 구현 방식은 담당이 결정</td></tr></table>
  <h3>구현과 기획이 어긋난 곳 정리</h3>
  <p>스킬 데이터테이블을 dev에 구현된 값과 맞춰 보니 액티브 스킬 63개가 전부 기본 쿨다운 18초였고, 랭크를 올려도 효과가 늘지 않게 랭크당 키 23개가 비어 있었습니다. 충돌 정리 시트로 근거를 남기고 담당별 요청 11건으로 나눠 전달했습니다.</p>
<h2 style="margin:44px 0 6px;color:var(--navy);font-size:24px">사례 1. 귀족 정책 카드: 문제에서 문서 세트까지 이틀</h2>

  <h3>문제</h3>
  <p>11월 9일 회의에서 귀족이 영지를 지키지 않고 기사를 따라다닌다는 문제가 나왔습니다. 원인은 귀족이 영지 안에서 할 콘텐츠가 부족한 것으로 정리됐고, 영지 안에서 할 일을 만드는 정책 카드를 기획했습니다.</p>
  <h3>핵심 규칙</h3>
  <table><tr><th style="width:20%">항목</th><th>규칙</th></tr>
   <tr><td>하루 흐름</td><td>낮 시작에 이벤트가 동시에 뜸. 최대 4개 수락(취소 불가), 완수하면 그 계열 카드 2장 중 1장. 하루 최대 3장 발동 후 소멸, 보유 6장, 남은 카드는 이월</td></tr>
   <tr><td>카드</td><td>21장, 계열 3개 (군사, 경제, 민생). 같은 계열 2장, 3장을 모으면 특수 효과와 세력 우호 +10</td></tr>
   <tr><td>수락과 우호</td><td>수락하지 않은 이벤트는 벌 없음, 수락한 뒤 실패하면 우호 −10. 3일 연속 방치하면 경고 사절</td></tr>
   <tr><td>전용 이벤트</td><td>하루 2개 (영지 안 1, 밖 1). 판정은 낮, 귀족은 돕는 역할</td></tr>
   <tr><td>업그레이드</td><td>대사관 Lv3, Lv5에서 수락 수나 보유 수 중 하나를 고름. 하루 발동 3장은 늘지 않음</td></tr>
   <tr><td>난이도 표시</td><td>별 1~3은 걸리는 시간, 칼은 전투, 왕관은 국왕 필요, 투구는 기사 필요. 이벤트마다 고정값</td></tr></table>
  <h3>만든 문서와 받는 사람</h3>
  <table><tr><th style="width:24%">문서</th><th style="width:18%">받는 사람</th><th>내용</th></tr>
   <tr><td>기획 초안</td><td>팀 전체</td><td>기획 의도, 기존 기능과의 관계, 흐름, 카드 목록, 민심 개편, 이벤트 목록</td></tr>
   <tr><td>데이터테이블 v1</td><td>구현, 수치</td><td>상수, 카드 21장, 묶음 보너스, 민심, 이벤트, 이벤트 난이도, 업그레이드</td></tr>
   <tr><td>UI 요청서</td><td>UI 기획</td><td>화면 요청 9건과 난이도 표시 레퍼런스. 새 아트 없이 기존 카드 형식 재사용</td></tr>
   <tr><td>구현 요청서</td><td>구현</td><td>구현 요청 9건, 구현 쪽에 확인할 질문 5건</td></tr>
   <tr><td>규칙 변경 요청</td><td>팀 전체</td><td>기존 규칙과 충돌하는 6건(R-65~R-70)을 현재 규칙, 변경 요청, 사유, 영향으로 정리</td></tr>
   <tr><td>대사관 건물 삭제 제안</td><td>팀 전체</td><td>정책 카드가 대사관 역할을 대신하게 되어 건물 삭제를 제안, 합의 완료</td></tr></table>
  <div class="lesson"><b>결과</b>11월 9일 회의 후 11일까지 문서 세트를 완성하고 dev에 반영했습니다(PR #357). 수치는 전부 임시값으로 두고 플레이테스트 뒤 확정하기로 했습니다.</div>
<h2 style="margin:44px 0 6px;color:var(--navy);font-size:24px">사례 2. 프롤로그 캠페인: 튜토리얼을 6장 이야기로</h2>

  <h3>왜 캠페인인가</h3>
  <p>10월 27일 회의에서 7단계 튜토리얼을 캠페인으로 바꾸기로 했습니다. 세 직업(국왕, 기사, 귀족)과 판 기능이 많아 한 번에 가르치면 놓치기 쉬워서, 장마다 기능을 하나씩 켜고 정해진 순서로 직업을 바꿔 가며 배우게 했습니다.</p>
  <h3>장별 흐름</h3>
  <table><tr><th style="width:12%">장</th><th style="width:9%">분</th><th style="width:13%">직업 전환</th><th>새로 가르치는 것</th></tr>
   <tr><td>1 함락</td><td>9.2</td><td>1번</td><td>이동, 화면, 공격, Q, 직업 전환</td></tr>
   <tr><td>2 피난처</td><td>11.8</td><td>4번</td><td>영지 창, 돈과 빵과 노동력 체인, 병영, 송금, 벽과 포탑</td></tr>
   <tr><td>3 피난처의 밤</td><td>6.6</td><td>4번</td><td>낮과 밤, 웨이브, 포탑 집중공격, 드래그와 어택땅, 스킬 배우기, W</td></tr>
   <tr><td>4 개척</td><td>12.2</td><td>5번</td><td>정찰, 사냥, 점령지, 망루, 마을 승격, 대장간, 무장, E</td></tr>
   <tr><td>5 동맹</td><td>10.1</td><td>7번</td><td>외교 창, 요청, 정책 카드, 칙령, 지원군 지휘, R</td></tr>
   <tr><td>6 탈환</td><td>8.5</td><td>8번</td><td>부대 지정과 호출</td></tr></table>
  <h3>설계 원칙</h3>
  <ul class="l"><li>판 기능은 장마다 하나씩 켭니다. 2장 영지, 3장 낮과 밤, 4장 필드, 5장 외교, 6장 부대 순서입니다.</li>
   <li>장 안에서는 경험치가 없고, 장 끝에 고정으로 지급해 다음 장의 스킬을 엽니다. 배운 스킬은 다음 장으로 이어집니다.</li>
   <li>안내 문구나 연출 없이 인물 대사로만 이야기를 전합니다. 스토리 작성 규칙을 문서로 따로 만들어 장마다 같은 기준으로 썼습니다.</li>
   <li>목표 시간 90분에 억지로 맞추지 않고, 장마다 계산한 시간(합계 58.4분)을 그대로 따랐습니다.</li>
   <li>장마다 체크포인트를 2~3곳 두고, 저장 대신 단계별 고정 상태로 다시 시작합니다.</li></ul>
  <div class="lesson"><b>회고</b>장별 세부 명세와 스크립트를 팀원 두 명에게 나눠 맡겼지만, 업무 범위만 전하고 기준을 문서로 주지 않아 결과물을 쓰지 못했습니다. 남은 기간에 직접 다시 작업해 6장을 완성했고, 그 뒤로는 지시서를 md 파일로 만들어 질문과 답을 문서로 주고받으며 방향을 맞췄습니다.</div>
  <h3>작업 문서 (27건)</h3>
<p class="note">팀 저장소에 남긴 본인 담당 문서를 읽기 쉽게 다시 편집했습니다. AI(Claude)로 초안과 표 정리를 하고, 기획 방향과 규칙, 수치 결정과 검토는 본인이 했습니다.</p>
<div class="doclist"><div class="dg"><b>정책 카드</b><a href="../files/aftermath/policy-card-plan.pdf">귀족 정책 카드 기획 초안 <small>10쪽</small></a><a href="../files/aftermath/policy-card-ui-request.pdf">귀족 정책 카드 UI 요청서 <small>6쪽</small></a><a href="../files/aftermath/policy-card-impl-request.pdf">귀족 정책 카드 구현 요청서 <small>12쪽</small></a></div><div class="dg"><b>프롤로그 캠페인</b><a href="../files/aftermath/campaign-overview.pdf">프롤로그 캠페인 전체 기획서 <small>7쪽</small></a><a href="../files/aftermath/campaign-ch1.pdf">프롤로그 캠페인 1장 세부기획서 <small>24쪽</small></a><a href="../files/aftermath/campaign-ch2.pdf">프롤로그 캠페인 2장 세부기획서 <small>24쪽</small></a><a href="../files/aftermath/campaign-ch3.pdf">프롤로그 캠페인 3장 세부기획서 <small>15쪽</small></a><a href="../files/aftermath/campaign-ch4.pdf">프롤로그 캠페인 4장 세부기획서 <small>19쪽</small></a><a href="../files/aftermath/campaign-ch5.pdf">프롤로그 캠페인 5장 세부기획서 <small>18쪽</small></a><a href="../files/aftermath/campaign-ch6.pdf">프롤로그 캠페인 6장 세부기획서 <small>17쪽</small></a></div><div class="dg"><b>국왕</b><a href="../files/aftermath/king-content-detail.pdf">국왕 콘텐츠 세부기획서 <small>17쪽</small></a><a href="../files/aftermath/king-automation-plan.pdf">국왕 자동화 기획서 <small>4쪽</small></a></div><div class="dg"><b>기사</b><a href="../files/aftermath/knight-plan.pdf">기사 추가 콘텐츠 기획서 <small>7쪽</small></a><a href="../files/aftermath/knight-detail.pdf">기사 콘텐츠 세부기획서 <small>11쪽</small></a></div><div class="dg"><b>귀족</b><a href="../files/aftermath/noble-plan.pdf">귀족 추가 콘텐츠 기획서 <small>13쪽</small></a><a href="../files/aftermath/noble-detail.pdf">귀족 콘텐츠 세부기획서 <small>19쪽</small></a></div><div class="dg"><b>유닛</b><a href="../files/aftermath/unit-detail.pdf">아군 NPC와 몬스터 유닛 세부기획서 <small>18쪽</small></a></div><div class="dg"><b>장비</b><a href="../files/aftermath/equipment-plan.pdf">장비 시스템 기획서 <small>7쪽</small></a><a href="../files/aftermath/equipment-datatable.pdf">장비 데이터테이블 v1 <small>6쪽</small></a><a href="../files/aftermath/equipment-impl-request.pdf">장비 구현 요청서 <small>7쪽</small></a><a href="../files/aftermath/equipment-art-request.pdf">장비 아트 요청서 <small>9쪽</small></a></div><div class="dg"><b>스킬</b><a href="../files/aftermath/skilltree-revision.pdf">스킬트리 보완 기획서 <small>12쪽</small></a><a href="../files/aftermath/skilltree-revision-impl.pdf">스킬트리 보완 구현 요청서 <small>11쪽</small></a></div><div class="dg"><b>튜토리얼</b><a href="../files/aftermath/tutorial-plan.pdf">튜토리얼 기획서 <small>18쪽</small></a><a href="../files/aftermath/tutorial-wireframe.pdf">튜토리얼 와이어프레임 <small>20쪽</small></a></div><div class="dg"><b>제안과 변경 요청</b><a href="../files/aftermath/conscription-proposal.pdf">징집 권한 이전 제안서 <small>6쪽</small></a><a href="../files/aftermath/embassy-removal-proposal.pdf">대사관 건물 삭제 제안 <small>6쪽</small></a></div></div>
</div></section>
''' + foot(1)
write('projects/aftermath.html', af)

# ---------------- 잔향 ----------------
ec = head('잔향 | 김준현', 1, 'home') + '''
<header class="phead"><div class="wrap"><div class="k">PROJECT 03 | 개인 프로젝트, Unity 6</div><h1>잔향 (Echo)</h1><p>"10초 전의 내가 지금의 동료가 된다", 시간 루프 퍼즐 플랫포머 (2026.09.11 ~ 09.18)</p></div></header>
<section class="s" style="padding-top:28px"><div class="wrap">
<div class="video" data-v="echo"><div class="ph" style="background:#3A4F7A"><div><b style="font-size:20px;color:#fff">잔향 플레이 영상</b><br>영상 준비 중</div></div></div>
<div class="stats"><div class="stat"><b>30</b><span>방 (스테이지 10 × 3)</span></div><div class="stat"><b>10+</b><span>기믹 종류</span></div><div class="stat"><b>5단계</b><span>방법별 도달 높이로 나눈 정답 루트</span></div><div class="stat"><b>1주</b><span>개발 기간</span></div></div>
<div class="gallery"><img src="../assets/img/echo-lobby.jpg" alt="스테이지 선택"><img src="../assets/img/echo-plate.jpg" alt="발판과 문"><img src="../assets/img/echo-tower.jpg" alt="2단 탑"><img src="../assets/img/echo-rewind.jpg" alt="되감기"><img src="../assets/img/echo-key.jpg" alt="열쇠와 장벽"><img src="../assets/img/echo-timeout.jpg" alt="시간 종료"></div>
<p class="cap">스테이지 선택, 발판과 문, 2단 탑, 되감기 연출, 스테이지 10 열쇠와 장벽, 시간 종료 선택. Windows 빌드 v1.0 화면.</p>
<h3>개요</h3>
<p>10초 동안의 움직임이 녹화되고, 되감으면 그 기록이 '잔향'이 되어 그대로 다시 움직인다. 과거의 내가 발판을 밟아 문을 열고, 닿지 않는 절벽은 과거의 나를 딛고 오른다. 목표 감정은 "내 계획이 맞아떨어지는 순간의 쾌감".</p>
<h3>담당 업무</h3>
<ul class="l"><li>컨셉 기획서, WBS 작성, 규칙 설계와 30개 방 레벨 디자인, 이동 방법별 수치 밸런싱</li>
<li>구현 (Claude 협업): 루프와 녹화 시스템, 기믹 10여 종, 로비, HUD, 되감기 연출, 에디터 스크립트로 30개 방 자동 생성</li></ul>
<h3>레벨 설계: 방법별 도달 높이</h3>
<table><tr><th>열쇠 든 점프</th><th>맨몸 점프</th><th>잔향 딛기</th><th>2단 탑</th><th>잔향 점프대</th></tr><tr><td>2.0</td><td>3.3</td><td>4.5</td><td>5.7</td><td>7.9</td></tr></table>
<p>절벽 높이를 두 값 사이로 정해 "이 방법이 아니면 오를 수 없는" 방을 만들었다. 방 1에서 새 요소를 소개하고 방 3에서 앞 요소를 조합한다.</p>
<h3>문제, 판단, 해결</h3>
<table><tr><th style="width:30%">문제</th><th style="width:30%">판단</th><th>해결</th></tr>
<tr><td>잔향 위에 서면 함께 떠오르는 버그</td><td>막기보다 퍼즐 재미로 쓸 수 있다</td><td>'잔향 점프대'를 정식 기믹으로 채택, 스테이지 4~5의 중심 규칙으로</td></tr>
<tr><td>후반 스테이지가 같은 풀이의 변주뿐</td><td>새로 배우는 규칙이 필요하다</td><td>'들면 점프가 낮아지는 열쇠'로 과거의 나에게 심부름 맡기는 퍼즐</td></tr>
<tr><td>마지막 방에서 의도보다 쉬운 풀이</td><td>감이 아닌 수치로 막아야 한다</td><td>점프 속도, 중력으로 이동 거리를 계산해 열쇠, 천장, 절벽 높이 조정</td></tr></table>
<h3>문서</h3>
<div class="docs"><a class="btn o" href="../files/echo-concept.pdf">컨셉 기획서 PDF</a><a class="btn o" href="../files/echo-wbs.pdf">WBS PDF</a></div>
<div class="lesson"><b>배운 점</b>기획서는 만드는 사람이 그대로 구현할 만큼 구체적이어야 하고, 의도는 수치와 조건으로 고정해야 지켜진다.</div>
</div></section>
''' + foot(1)
write('projects/echo.html', ec)

# ---------------- WHO AM I ----------------
wa = head('WHO AM I? | 김준현', 1, 'home') + '''
<header class="phead"><div class="wrap"><div class="k">PROJECT 04 | 팀 프로젝트</div><h1>WHO AM I?</h1><p>감정 곡선 레벨 설계</p></div></header>
<section class="s" style="padding-top:28px"><div class="wrap">
<h3 style="margin-top:0">WHO AM I?: 추리 미스터리 비주얼 노벨 (5인 팀, 1주, 2026.04)</h3>
<p><b>역할:</b> 시스템, 레벨 디자인, 여섯 방의 감정 곡선과 배치 순서, 방별 조사 루프, 아이템, 상호작용 조건 설계, 팀원이 그대로 구현할 수 있는 조건 문서 작성</p>
<div class="docs"><a class="btn o" href="../files/whoami-level-design.pdf">시스템 & 레벨 디자인 기획서 PDF</a></div>
<div class="gallery"><img src="../assets/img/who-title.jpg" alt="타이틀"><img src="../assets/img/who-lobby.jpg" alt="로비"><img src="../assets/img/who-101.jpg" alt="101호 언제 (호감)"><img src="../assets/img/who-103.jpg" alt="103호 무엇 (의심, 불안)"><img src="../assets/img/who-106.jpg" alt="106호 누가 (혼란, 선택)"><img src="../assets/img/who-choice.jpg" alt="마지막 선택"></div>
<p class="cap">타이틀, 로비, 101호(호감), 103호(의심, 불안), 106호(혼란, 선택), 마지막 선택. 방이 진행될수록 배경이 낡고 어두워진다. 이미지와 구현은 팀 공동 작업이다.</p>
<h3>팀 내 역할 (5인, 렌파이, 2026.04.20 ~ 26)</h3>
<table><tr><th style="width:30%">역할</th><th style="width:16%">담당</th><th>범위</th></tr>
<tr><td>일정 관리</td><td>팀원</td><td>팀 일정과 작업 보드 관리</td></tr>
<tr><td>시나리오</td><td>팀원</td><td>세계관과 메인 시나리오</td></tr>
<tr><td><b>시스템, 레벨 디자인</b></td><td><b>본인</b></td><td><b>플레이 루프, 로비 구조, 여섯 방의 감정 단계와 배치 순서, 방별 상호작용 조건</b></td></tr>
<tr><td>이미지 리소스</td><td>팀원</td><td>배경, 캐릭터, UI 이미지</td></tr>
<tr><td>스크립트</td><td>팀원</td><td>장면별 스크립트와 분기</td></tr></table>
<h3>감정 설계: 여섯 방의 배치 순서</h3>
<div class="fig"><img src="../assets/img/whoami_emotion.svg" alt="감정 단계별 여섯 방 배치"></div>
<table><tr><th style="width:18%">단계</th><th style="width:20%">방</th><th>설계</th></tr>
<tr><td>1. 호감</td><td>언제, 어디서</td><td>인물 정보 없이 배경만 서술해 분위기에 몰입시키고 NPC에게 호감을 갖게 함</td></tr>
<tr><td>2. 의심, 불안</td><td>무엇을, 어떻게</td><td>사건의 실마리를 드러내 1단계의 호감과 부딪히게 함</td></tr>
<tr><td>3. 혼란, 선택</td><td>왜, 누가</td><td>NPC 정체를 공개하는 '누가'를 마지막 방에 두어 엔딩 선택(기획 3종, 일정상 2종 구현)에 직결</td></tr></table>
<h3>플레이 루프</h3>
<div class="fig" style="max-width:640px"><img src="../assets/img/whoami_loop.svg" alt="조사, 아이템 획득, 해금, 단서 확인 루프"></div>
<p>조사, 아이템 획득, 해금, 단서 확인 루프. 스토리 전달이 핵심이라 퍼즐 난이도는 낮추고, 탐색하는 동안 추측이 쌓이도록 했다.</p>
<h3>레벨 설계 슬라이드</h3>
<div class="slides"><iframe src="https://docs.google.com/presentation/d/11o8cVJIv6a7kVMNV6VL-Kx9cTSWrfof7U1WdUt_ZhTg/embed?start=false&loop=false" allowfullscreen loading="lazy" title="WHO AM I? 레벨 설계 슬라이드"></iframe></div>
<div class="docs"><a class="btn o" href="https://docs.google.com/presentation/d/11o8cVJIv6a7kVMNV6VL-Kx9cTSWrfof7U1WdUt_ZhTg/view">새 창에서 보기</a></div>
</div></section>
''' + foot(1)
write('projects/whoami.html', wa)

# ---------------- 소개 ----------------
ab = head('소개 | 김준현', 0, 'about') + f'''
<header class="phead"><div class="wrap"><div class="k">ABOUT</div><h1>김준현</h1><p>오래 남는 순간은 우연이 아니라 설계입니다.</p></div></header>
<section class="s"><div class="wrap"><div class="about">
<img class="ph" src="assets/img/photo.png" alt="김준현">
<div>
<p style="font-size:18px;color:var(--navy);font-weight:700">'플레이어가 이 순간 무엇을 느껴야 하는가'부터 정하고, 그 감정이 생기도록 규칙과 레벨을 거꾸로 짭니다.</p>
<p>방송연예학과에서 연극 연출을 하며, 한 장면의 감정을 위해 조명과 음향의 타이밍, 배우의 동선을 계속 연구했습니다. 그 경험을 플레이어가 직접 움직이는 게임에서 쓰고 싶어 게임 기획을 시작했습니다.</p>
<div class="chips"><span class="chip">감정 곡선 기반 레벨 설계</span><span class="chip">수치로 해법을 강제하는 퍼즐</span><span class="chip">바로 구현되는 기획서</span><span class="chip">연출 전공의 장면 구성 감각</span><span class="chip">한순간을 위한 빌드업 설계</span></div>
<div class="btns"><a class="btn o" href="mailto:junhyeon.kim.work@gmail.com">junhyeon.kim.work@gmail.com</a></div>
</div></div>

<h3>걸어온 길</h3>
<div class="tl">
<div><b>2026.04 ~ 12</b> 디벨로켓(경일게임아카데미) 게임 기획 교육과정 (2026.12 수료 예정): Aftermath, 잔향, WHO AM I?, 메모리 엔더</div>
<div><b>2025.11 ~ 2026.03</b> 오진양행 서비스사업부: 커피머신 방문 수리, 점검 및 고장 원인 진단</div>
<div><b>2023.02</b> 가톨릭관동대학교 방송연예학과 연출전공 학사 졸업</div>
<div><b>2021</b> 정기공연 '벚꽃동산' 연출, 30명, 2개월, 40석 7회 전석 만석 / 극단 임영씨어터 대표로 '하멜린' 기획, 운영, 정산</div>
<div><b>2019</b> 정기공연 '임차인' 첫 연출 (7회)</div>
</div>

<h3>일하는 방식</h3>
<table><tr><th style="width:18%">단계</th><th>방식</th></tr>
<tr><td>규칙부터</td><td>작업 전에 목표 감정과 지킬 규칙을 문서로 먼저 정하고, 이후 결정은 그 문서를 기준으로 내린다</td></tr>
<tr><td>동기화</td><td>팀 작업은 깃허브, Jira, Confluence에서 진행 상황부터 맞춘다. 팀원 작업물을 건드리지 않도록 올리는 절차를 정해 두고 지킨다</td></tr>
<tr><td>토론</td><td>초안을 내면 안 되는 이유부터 반론을 받아 보고, 남는 것만 결정한다</td></tr>
<tr><td>검증</td><td>간단히 구현해 직접 플레이하며 조정한다. 재미와 감정은 내가 판단한다</td></tr></table>

<h3>AI 활용</h3>
<p>코드와 문서 초안은 Claude와 함께 만들었고, 기획과 규칙, 수치 결정, 플레이 검증은 직접 했습니다.</p>

<h3>도구</h3>
<div class="chips"><span class="chip">Unity 6</span><span class="chip">VS Code</span><span class="chip">Git</span><span class="chip">Claude, Claude Code</span><span class="chip">Jira</span><span class="chip">Confluence</span><span class="chip">Notion</span><span class="chip">Excel</span><span class="chip">PowerPoint</span></div>
</div></section>

<section class="s alt"><div class="wrap">
<h2 class="t">프로젝트 다시 보기</h2><p class="st">궁금한 프로젝트를 골라 기획 의도와 설계 과정을 확인해 보세요.</p>
<div class="cards">{''.join(card(pr, '') for pr in PROJECTS)}</div>
</div></section>
''' + foot(0)
write('about.html', ab)

# ---------------- 게임 분석 ----------------
an = head('게임 분석 및 제안 | 김준현', 0, 'analysis') + '''
<header class="phead"><div class="wrap"><div class="k">GAME ANALYSIS &amp; PROPOSAL</div><h1>게임 분석 및 제안</h1><p>잘 만든 상용 게임이 감정을 어디서 쌓고 어디서 터뜨리는지 뜯어 봅니다. 분석에서 찾은 구조를 바탕으로, 그 게임에 더할 새 콘텐츠도 함께 제안합니다.</p></div></header>
<section class="s"><div class="wrap">
<div class="cards">
<div class="card"><div class="thumb"><div class="txt" style="background:#2F5496">트릭컬 리바이브</div></div><div class="c"><div class="tag">ANALYSIS 01 | 수집형 RPG</div><h4>트릭컬 리바이브</h4><p>분석 문서 준비 중입니다.</p></div></div>
</div>
</div></section>
''' + next_block('analysis', 0) + foot(0)
write('analysis.html', an)
print('ok')
