import shutil, os
A = '/home/claude/portfolio/assets/img/'
I = '/home/claude/pdfwork/img/'
SITE = 'kim-junhyeon.github.io/portfolio'
EMAIL = 'junhyeon.kim.work@gmail.com'
ID = '오래 기억될 한순간, 그 순간까지의 감정과 규칙, 수치를 설계하는 콘텐츠, 시스템 기획자'

css = '''
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:'Noto Sans CJK KR',sans-serif;color:#222;font-size:8.6pt;line-height:1.55}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always}
.hdr{background:#1B2A4A;color:#fff;padding:9mm 13mm 7mm;position:relative}
.hdr .k{font-size:6.6pt;letter-spacing:.28em;color:#aab6d0}
.hdr h2{font-size:20pt;margin:2mm 0 1.5mm;font-weight:700}
.hdr .q{font-size:9pt;color:#dfe5f1}
.hdr .tag{position:absolute;right:13mm;top:9mm;text-align:right;font-size:7.5pt;color:#dfe5f1;line-height:1.6}
.body{padding:6mm 13mm 0}
.stats{display:flex;gap:4mm;margin:1mm 0 4mm}
.stat{flex:1;border:1px solid #d5dae3;border-radius:3px;text-align:center;padding:3.2mm 1mm}
.stat b{display:block;font-size:15pt;color:#1B2A4A;line-height:1.2}
.stat span{font-size:6.8pt;color:#666}
.links{background:#eef1f6;border-radius:3px;padding:2.2mm 3.5mm;font-size:7.6pt;margin-bottom:3mm;line-height:1.75}
.links b{color:#1B2A4A;margin-right:1mm}
.links a{color:#2F5496;text-decoration:none}
table{border-collapse:collapse;width:100%;margin:1.5mm 0 3mm}
td,th{border:1px solid #d5dae3;padding:1.5mm 2.2mm;vertical-align:top;text-align:left;font-size:7.8pt}
th{background:#1B2A4A;color:#fff;font-weight:700}
th small{display:block;font-weight:400;color:#c9d2e4;font-size:6.6pt}
table.info td.h{background:#eef1f6;font-weight:700;color:#1B2A4A;width:12%}
h5{font-size:9.6pt;color:#1B2A4A;margin:3.5mm 0 1.5mm;border-left:3px solid #1B2A4A;padding-left:2.2mm}
p{margin:1mm 0}
ul{margin:1mm 0 2mm 4mm;padding:0}li{margin:.4mm 0}
.fig img{width:100%;display:block}
.gal{display:flex;gap:3mm;margin:2mm 0 1mm}.gal div{flex:1;text-align:center;font-size:6.8pt;color:#555}
.gal img{width:100%;border-radius:2px;display:block;margin-bottom:1mm}
.box{background:#1B2A4A;color:#fff;border-radius:3px;padding:3mm 4mm;margin:3mm 0;font-size:8pt}
.box b{color:#9fc0ff;margin-right:2mm}
.gbox{background:#eef1f6;border-radius:3px;padding:2.5mm 4mm;margin:3mm 0;font-size:8pt}
.gbox b{color:#1B2A4A;margin-right:2mm}
.foot{position:absolute;left:13mm;right:13mm;bottom:7mm;border-top:1px solid #d5dae3;padding-top:2mm;display:flex;justify-content:space-between;font-size:6.6pt;color:#888}
.small{font-size:7.2pt;color:#555}
/* cover */
.cov{background:#1B2A4A;color:#fff;padding:18mm 13mm 14mm;height:98mm}
.cov .k{font-size:7pt;letter-spacing:.35em;color:#aab6d0}
.cov h1{font-size:30pt;margin:5mm 0 3mm}
.cov .t{font-size:12pt;font-weight:700}
.cov .s{font-size:8.6pt;color:#dfe5f1;margin-top:1.5mm}
.cov .c{font-size:7.6pt;color:#c9d2e4;margin-top:9mm}
.sec{font-size:7.4pt;letter-spacing:.3em;font-weight:700;color:#1B2A4A;border-bottom:1.5px solid #1B2A4A;padding-bottom:1.5mm;margin:8mm 0 4mm}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.card{border:1px solid #d5dae3;border-radius:4px;padding:4mm;position:relative}
.card.hl{border-color:#2F5496;background:#f4f7fc}
.card .n{font-size:15pt;color:#9fb3d6;font-weight:700}
.card .pg{position:absolute;right:4mm;top:4mm;font-size:6.8pt;color:#888}
.card h4{font-size:10.5pt;margin:.5mm 0;color:#1B2A4A}
.card .m{font-size:6.8pt;color:#666;margin-bottom:1.5mm}
.card p{font-size:7.6pt}
.card .nums{margin-top:2mm;font-size:6.8pt;color:#666}.card .nums b{color:#1B2A4A;font-size:10pt;margin:0 1mm 0 0}
span.c{}
.lk td:first-child{background:#eef1f6;font-weight:700;color:#1B2A4A;width:15%}
.bars{display:flex;align-items:flex-end;gap:5mm;height:30mm;margin:2mm 0 1mm;padding:0 2mm}
.bar{flex:1;text-align:center}
.bar div{background:#2F4A85;color:#fff;font-size:7pt;padding-top:1mm}
.bar span{display:block;font-size:6.8pt;color:#444;margin-top:1mm}
'''

def foot(right):
    return f'<div class="foot"><span>김준현 | 게임 기획 포트폴리오 | {SITE}</span><span>{right}</span></div>'

def hdr(k, h, q, tag=''):
    t = f'<div class="tag">{tag}</div>' if tag else ''
    return f'<div class="hdr">{t}<div class="k">{k}</div><h2>{h}</h2><div class="q">{q}</div></div>'

def img(path):
    return 'file://' + path

pages = []

# 1 cover
pages.append(f'''<section class="page">
<div class="cov"><div class="k">GAME DESIGN PORTFOLIO</div><h1>김준현</h1>
<div class="t">오래 남는 순간은 우연이 아니라 설계입니다.</div>
<div class="s"><span class="c">{ID}</span></div>
<div class="c"><span class="c">{EMAIL} &nbsp;| &nbsp;{SITE}</span></div></div>
<div class="body" style="padding-top:0">
<div class="sec">CONTENTS</div>
<div class="cards">
<div class="card hl"><span class="pg">2~3쪽</span><div class="n">01</div><h4>메모리 엔더</h4><div class="m">개인, 웹 게임(Phaser 3), 기획 전반 + AI 협업 구현, 2026.11 (6일)</div>
<p>기억을 지우는 장의사가 장례를 거부한 망자를 쫓는다. 추리, 추격, 장례로 감정을 쌓아 클라이맥스에서 터뜨리는 구조.</p>
<div class="nums"><span class="c"><b>35</b>튜닝 기록</span> &nbsp; <b>3</b>구간 &nbsp; <span class="c"><b>6일</b>기획, 구현, 배포</span></div></div>
<div class="card"><span class="pg">4~6쪽</span><div class="n">02</div><h4>Aftermath</h4><div class="m">팀(5인), Unity, <span class="c">컨셉 원안, 콘텐츠 기획, 2026.09 ~ 12</span></div>
<p>3인 온라인 협동 타워 디펜스. 스킬트리, 장비, 정책 카드, 프롤로그 캠페인을 기획하고 기획서, 데이터테이블, 요청서 순으로 구현까지 전달.</p>
<div class="nums"><b>40+</b>기획 문서 &nbsp; <b>37</b>Jira 이슈</div></div>
<div class="card"><span class="pg">7쪽</span><div class="n">03</div><h4>잔향 (Echo)</h4><div class="m">개인, Unity 6, 기획 전반 + AI 협업 구현, 2026.09 (1주)</div>
<p>"10초 전의 내가 지금의 동료가 된다." 녹화한 움직임을 재생해 푸는 시간 루프 퍼즐 플랫포머.</p>
<div class="nums"><b>30</b>방 &nbsp; <b>10+</b>기믹</div></div>
<div class="card"><span class="pg">8쪽</span><div class="n">04</div><h4>WHO AM I?</h4><div class="m">팀(5인), Ren'Py, 시스템, 레벨 디자인, 2026.04 (1주)</div>
<p>육하원칙 여섯 방을 호감, 의심, 혼란, 선택의 감정 순서로 배치한 추리 비주얼 노벨.</p>
<div class="nums"><b>6</b>방 &nbsp; <b>3</b>엔딩</div></div>
</div>
<div class="sec">LINKS</div>
<table class="lk">
<tr><td>게임</td><td>sei-ban.github.io/memory-ender (설치 없이 브라우저, 챕터 선택 가능)</td></tr>
<tr><td>사이트</td><td><span class="c">{SITE} (프로젝트 상세, 게임 분석 및 제안, 영상, 소개)</span></td></tr>
<tr><td>기획서</td><td><span class="c">{SITE}/files/memory-ender-gdd.pdf</span> (메모리 엔더 게임 기획서 15쪽)</td></tr>
</table>
<p class="small">AI(Claude)를 활용한 범위와 본인이 맡은 범위는 8쪽 'AI 활용 범위 명시'에 정리했습니다.</p>
</div></section>''')

# 2 memory ender 1
pages.append(f'''<section class="page">
{hdr('PROJECT 01 | 개인 프로젝트','메모리 엔더 (Memory Ender)','기억을 지우는 장의사가 장례를 거부한 망자를 쫓아, 마지막 장례를 치른다','웹 게임 (PC)<br>현재 빌드: 첫 에피소드')}
<div class="body">
<div class="stats"><div class="stat"><b>3구간</b><span>추리, 추격, 장례</span></div><div class="stat"><b>35</b><span>플레이 튜닝 항목</span></div><div class="stat"><b>약 5분</b><span>첫 에피소드</span></div><div class="stat"><b>1인 + AI</b><span>기획, AI 협업 구현</span></div></div>
<div class="links"><b>플레이</b><a>https://sei-ban.github.io/memory-ender/</a> (설치 없이 브라우저, 챕터 선택 가능, 클라이맥스는 3. 장례)<br><b>상세, 영상</b><a><span class="c">{SITE}/projects/memory-ender</span></a> &nbsp; <b>기획서</b><a>PDF</a> &nbsp; <b>저장소</b><a>github.com/sei-ban/memory-ender</a></div>
<table class="info"><tr><td class="h">기간</td><td>2026.11.19 ~ 24 (6일): 기획, 구현, 아트, 웹 배포</td><td class="h">역할</td><td>1인, 기획 전반 + AI 협업 구현</td></tr>
<tr><td class="h">장르</td><td>스토리 중심 액션 어드벤처</td><td class="h">사용 툴</td><td>Claude, Claude Code, Git, GitHub Pages</td></tr></table>
<h5>기획 의도</h5>
<p>빌드업을 쌓아 클라이맥스에서 터지는 한순간이 핵심 재미이며, 그 순간이 플레이를 계속하게 만든다. 중심 감정은 <b>연민과 갈등</b>이다. 지워야 한다는 걸 알지만 지우고 싶지 않은 마음을, 플레이어가 마지막에 <b>자기 손으로</b> 결정하게 만든다.</p>
<h5>목표 감정 곡선</h5>
<div class="fig"><img src="{img(I+'p-000.png')}" style="width:88%;margin:0 auto"></div>
<h5>빌드업 구조: 구간마다 쌓는 감정과 장치</h5>
<table><tr><th style="width:12%">구간</th><th style="width:20%">쌓이는 감정</th><th>기대 장치<small>다음이 궁금해지게 만드는 것</small></th><th style="width:27%">방해 장치<small>쉽게 풀리지 않게 하는 것</small></th></tr>
<tr><td><b>추리</b></td><td>사명감에서 관계 추측으로</td><td>단서 3개로 관계가 조금씩 드러남 (결과, 장소, 동기 순)</td><td>신호로만 위치를 앎, 오답이면 다시 추리</td></tr>
<tr><td><b>추격</b></td><td>긴박감 + 연민의 시작</td><td>망자를 맞힐 때마다 기억 문장(주마등) 공개. 웃던 밤에서 싸우기 직전의 밤 순서</td><td><span class="c">망자의 회피 패턴 3종</span>, 붕괴 지형, 잔해</td></tr>
<tr><td><b>장례</b></td><td>갈등</td><td>갑옷 파츠를 뜯을 때마다 둘의 기억 장면으로 전환</td><td>끌어당기는 저항감, 순서 고정</td></tr>
<tr><td><b>클라이맥스</b></td><td>연민과 갈등의 정점</td><td>데이터 망자를 누르는 동안 마지막 독백 진행</td><td>손을 떼면 멈춤. 끝낼지는 플레이어가 쥐고 있음</td></tr></table>
</div>{foot('메모리 엔더 1 / 2')}</section>''')

# 3 memory ender 2
pages.append(f'''<section class="page">
{hdr('PROJECT 01 | 메모리 엔더','설계, 플레이, 수정의 반복과 AI와의 역할 분담','')}
<div class="body">
<div class="gal"><div><img src="{img(I+'p-001.jpg')}">추격: 기억을 빨아들이는 연타</div><div><img src="{img(I+'p-002.jpg')}">장례: 갑옷을 뜯을 때 나오는 기억 장면</div><div><img src="{img(I+'p-003.jpg')}">클라이맥스: 데이터 망자를 지우는 9초</div></div>
<h5>클라이맥스 설계</h5>
<p><span class="c">갑옷(기억)</span> 5개를 모두 뜯어내면 <span class="c">데이터 망자(데이터가 된 망자의 형체)</span>만 남는다. 조등(장의사의 장례 도구)을 대고 <b>누르고 있는 9초</b> 동안 마지막 독백 3줄이 흐르고, 손을 떼면 멈춘다. 마지막 줄 "다음 편은… 혼자 봐야 할 거 같아."는 추격의 주마등 "다음 편은 내일 같이 보자."를 회수한다. 이후 현실의 방에서 그녀는 혼자 소파에 앉아, 이유 모를 허전함을 느낀다.</p>
<h5>문제, 판단, 해결 (튜닝 기록 35항목 중)</h5>
<table><tr><th style="width:30%">문제 (플레이하며 느낀 점)</th><th style="width:30%">판단</th><th>해결</th></tr>
<tr><td>장례가 단순 홀드라 아무 감정도 전달되지 않음</td><td>지우는 행위 자체가 감정을 만들어야 한다</td><td>기사의 갑옷 파츠를 정해진 순서로 <b>직접 붙잡고 뜯어내는 조작</b>으로 재설계</td></tr>
<tr><td><span class="c">망자를 붙잡는 포착 링</span> 2초가 늘어져 긴박감이 없음</td><td>추격의 리듬을 해치는 늘어짐 제거</td><td><span class="c">포착 링 2초를 <b>1초</b>로, 붙잡은 뒤 흡수는 길게 누르기에서</span> <b>3초 안에 연타 10회</b>로</td></tr>
<tr><td>가시, 함정, 공격이 겹쳐 무조건 맞는 순간</td><td>불합리하게 지면 쌓아 온 몰입이 깨진다</td><td>기믹이 겹치지 않게 배치, 회피 전 <b>0.4초 예고</b></td></tr>
<tr><td>문구만으로는 둘에게 무슨 일이 있었는지 와닿지 않음</td><td>보여 주는 것이 읽히는 것보다 강하다</td><td>파츠를 뜯을 때마다 <b>기억 장면으로 화면 전환</b> (5초)</td></tr>
<tr><td>주마등 문장이 흡수 완료 시점에 나옴</td><td>망자가 맞은 타이밍에 나와야 한다</td><td>공개 시점을 <b>명중 순간</b>으로 이동 (2.6초)</td></tr></table>
<h5>AI 협업: 역할 분담</h5>
<table><tr><th style="width:15%">영역</th><th style="width:45%">본인</th><th>AI (Claude)</th></tr>
<tr><td>기획, 설계</td><td>세계관, 스토리, 감정 설계, 조작 규칙, 클라이맥스 구조 결정</td><td>선택지 제시, 문구 초안 2~3안</td></tr>
<tr><td>구현</td><td>플레이 테스트, 버그, 불편 판단</td><td>코드 작성, 사운드 합성, 자동 플레이 테스트</td></tr>
<tr><td>튜닝</td><td>직접 플레이 후 수치, 규칙 변경 결정, 이유 작성</td><td>요청한 변경을 즉시 빌드에 반영</td></tr>
<tr><td>문서</td><td>기획 의도, 판단 근거, 최종 확정</td><td>표, 서식 정리, 확정 내용 초안</td></tr></table>
<p class="small">AI 초안을 그대로 쓰지 않은 사례: 장례 단순 홀드를 반려하고 갑옷 뜯기로 재설계 / 세계관과 어긋난 단서, 스토리 초안을 직접 수정 / AI가 임의로 뺀 '누르기' 조작을 복구하고 "사용자가 정한 구조는 AI가 바꾸지 않는다"는 작업 규칙 추가</p>
<h5>작업 방식</h5>
<ul><li><b>규칙부터:</b> 작업 방향을 정하는 세션을 먼저 열어 규칙 문서를 만들고 프로젝트에 넣어 둔다</li>
<li><b>토론:</b> 내 초안을 주고 이유와 안 되는 점을 반론하게 한 뒤 결정한다</li>
<li><b>검증:</b> 간단히 구현해 직접 플레이하며 조정한다. 재미와 감정은 내가 판단한다</li></ul>
<div class="box"><b>배운 점</b>수치에 약해 숫자만으로는 판단이 안 됐지만, AI로 바로 만들어 직접 플레이하며 수치와 타이밍을 고치는 방식으로 그 약점을 보완했다.</div>
</div>{foot('메모리 엔더 2 / 2')}</section>''')

AFH = lambda q: hdr('PROJECT 02 | 팀 프로젝트','Aftermath',q,'Unity<br>2026.09 ~ 12')

# 4 aftermath 1
pages.append(f'''<section class="page">
{AFH('3인 온라인 협동 타워 디펜스')}
<div class="body">
<div class="stats"><div class="stat"><b>40+</b><span>작성한 기획 문서</span></div><div class="stat"><b>73</b><span>규칙 변경 요청, 명세 반영</span></div><div class="stat"><b>37</b><span>Jira 담당 이슈</span></div><div class="stat"><b>10</b><span>1차 빌드 구현 PR</span></div></div>
<table class="info"><tr><td class="h">기간</td><td>2026.09 ~ 12 (12.04 발표회)</td><td class="h">역할</td><td><span class="c">컨셉 원안, 콘텐츠 기획 (5인 팀)</span></td></tr>
<tr><td class="h">장르</td><td>3인 온라인 협동 타워 디펜스 (PC)</td><td class="h">사용 툴</td><td>Unity, Jira, Confluence, Git, Claude</td></tr></table>
<h5>담당한 콘텐츠</h5>
<table><tr><th style="width:20%">콘텐츠</th><th style="width:47%">한 일</th><th>숫자</th></tr>
<tr class="cr"><td>게임 컨셉 원안</td><td>국왕, 귀족, 기사가 국고, 마나, 영토를 하나씩 쥐고 서로 주고받으며 막아 내는 3인 협동 디펜스 원안(컨셉 아이데이션 문서)을 냈고, 팀이 이를 기준으로 컨셉 원페이저를 만들었다</td><td>역할 3개, 자원 3개</td></tr>
<tr><td>스킬트리</td><td>스킬 상세 기획, 데이터테이블을 구현값에 맞춰 정리, 단일 대상 스킬을 범위형으로 보완</td><td>데이터테이블 v7, 담당별 요청 11건</td></tr>
<tr><td>튜토리얼</td><td>단계 흐름 기획과 화면 와이어프레임, 이후 캠페인 방식으로 전환</td><td>7단계</td></tr>
<tr><td>국왕, 기사, 귀족 추가 콘텐츠</td><td>직업별 세부기획서, 데이터테이블, <span class="c">UI 요청서</td><td>국왕</span> 데이터테이블 v8</td></tr>
<tr><td>장비 시스템</td><td>슬롯, 일반 장비와 특수 장비, <span class="c">부여(제작할 때 재료를 더해 효과를 붙임)와 특화 부여(특정 적에게 피해 증가)</span>, 아트 요청</td><td>일반 6종, 특수 24종, 아이콘 36종</td></tr>
<tr><td>국왕 자동화</td><td>영지 단계와 생산 체인 자동화, 가공 대기열 조정</td><td>영지 4단계, 대기열 5칸에서 10칸</td></tr>
<tr><td>귀족 정책 카드</td><td>낮 이벤트를 완수해 카드를 받고 발동하는 영지 안 콘텐츠 (5쪽 사례)</td><td>카드 21장, 계열 3개</td></tr>
<tr><td>프롤로그 캠페인</td><td>6장 전체 흐름과 장별 세부기획 (6쪽 사례)</td><td>6장, 계산 58.4분</td></tr></table>
<h5>구현 담당이 바로 작업할 수 있는 전달 방식</h5>
<table><tr><th style="width:20%">단계</th><th>내용</th></tr>
<tr><td>기획서</td><td>규칙, 예외, 수치의 의도를 먼저 쓰고 상세는 표로</td></tr>
<tr><td>데이터테이블</td><td>수치의 원본. 기획서보다 우선하도록 버전 관리</td></tr>
<tr class="cr"><td>규칙 변경 요청서</td><td>기존 규칙과 충돌하는 변경은 요청서에 번호를 붙여 현재 규칙, 바꿀 내용, 이유, 영향을 정리. 팀 전원이 확인 기록을 남기면 명세에 반영하고 구현, 문제가 있으면 수정할 부분을 돌려받아 다시 기획 (73건)</td></tr>
<tr><td>구현, UI, 아트 요청서</td><td>받는 사람별로 나눠 무엇을, 왜, 어떤 우선순위로 할지만 전달. 구현 방식은 담당이 결정</td></tr></table>
<h5>구현과 기획이 어긋난 곳 정리</h5>
<p>스킬 데이터테이블을 <span class="c">개발 빌드에 구현된 값</span>과 맞춰 보니 액티브 스킬 63개가 전부 기본 쿨다운 18초였고, <span class="c">랭크별 수치 23칸이 비어 있어 랭크를 올려도 효과가 늘지 않았습니다</span>. 충돌 정리 시트로 근거를 남기고 담당별 요청 11건으로 나눠 전달했습니다.</p>
</div>{foot('Aftermath 1 / 3')}</section>''')

# 5 aftermath 2
pages.append(f'''<section class="page">
{AFH('사례 1. 귀족 정책 카드: 문제에서 문서 세트까지 이틀')}
<div class="body">
<div style="display:flex;gap:6mm;align-items:flex-start"><div style="flex:1.45"><h5>문제</h5><p>11월 9일 회의에서 귀족이 영지를 지키지 않고 기사를 따라다닌다는 문제가 나왔습니다. 원인은 귀족이 영지 안에서 할 콘텐츠가 부족한 것으로 정리됐고, 영지 안에서 할 일을 만드는 정책 카드를 기획했습니다.</p></div>
<div style="flex:1;text-align:center;font-size:6.8pt;color:#555;margin-top:3mm"><img src="{img(I+'p-004.jpg')}" style="width:100%;border-radius:2px">외교 창: 수락한 일을 완수하면 카드 보상</div></div>
<h5>핵심 규칙</h5>
<table><tr><th style="width:20%">항목</th><th>규칙</th></tr>
<tr><td>하루 흐름</td><td>낮 시작에 이벤트가 동시에 뜸. 최대 4개 수락(취소 불가), 완수하면 그 계열 카드 2장 중 <span class="c">1장을 고름</span>. 하루 최대 3장 발동 후 소멸, 보유 6장, 남은 카드는 이월</td></tr>
<tr><td>카드</td><td>21장, 계열 3개 (군사, 경제, 민생). 같은 계열 2장, 3장을 모으면 특수 효과와 세력 우호 +10</td></tr>
<tr><td>수락과 우호</td><td>수락하지 않은 이벤트는 벌 없음, 수락한 뒤 실패하면 우호 −10. <span class="c">세력 요청을 3일 연속 수락하지 않으면 그 세력이 경고 사절을 보냄</span></td></tr>
<tr><td><span class="c">외교 이벤트</td><td>하루 2개 (영지 안 1, 밖 1). 모두 낮에 판정하고 기한은 그날 밤 시작. 처치 조건은 누가 처치해도 인정 (귀족은 돕는 역할)</span></td></tr>
<tr><td>업그레이드</td><td>대사관 Lv3, Lv5에서 수락 수나 보유 수 중 하나를 고름. 하루 발동 3장은 늘지 않음</td></tr>
<tr><td>난이도 표시</td><td>별 1~3은 걸리는 시간, 칼은 전투, 왕관은 국왕 필요, 투구는 기사 필요. 이벤트마다 고정값</td></tr></table>
<h5>만든 문서와 받는 사람</h5>
<table><tr><th style="width:22%">문서</th><th style="width:16%">받는 사람</th><th>내용</th></tr>
<tr><td>기획 초안</td><td>팀 전체</td><td>기획 의도, 기존 기능과의 관계, 흐름, 카드 목록, <span class="c">민심 시스템 개편</span>, 이벤트 목록</td></tr>
<tr><td>데이터테이블 v1</td><td><span class="c">구현 담당, 레벨 디자인</span></td><td><span class="c">공통 설정값</span>, 카드 21장, <span class="c">계열 묶음 보너스</span>, 민심, 이벤트, 이벤트 난이도, 업그레이드</td></tr>
<tr><td>UI 요청서</td><td>UI 기획</td><td>화면 요청 9건과 난이도 표시 레퍼런스. 새 아트 없이 기존 카드 형식 재사용</td></tr>
<tr><td>구현 요청서</td><span class="c"><td>구현 담당</td></span><td>구현 요청 9건, 구현 쪽에 확인할 질문 5건</td></tr>
<tr><td>규칙 변경 요청</td><td>팀 전체</td><td>기존 규칙과 충돌하는 6건을 현재 규칙, 변경 요청, 사유, 영향으로 정리</td></tr>
<tr><td>대사관 건물 삭제 제안</td><td>팀 전체</td><td>정책 카드가 대사관 역할을 대신하게 되어 건물 삭제를 제안, 합의 완료</td></tr></table>
<div class="box"><b>결과</b>11월 9일 회의 후 11일까지 문서 세트를 완성하고 <span class="c">개발 빌드에 반영했습니다</span>. 수치는 전부 임시값으로 두고 플레이테스트 뒤 확정하기로 했습니다.</div>
</div>{foot('Aftermath 2 / 3')}</section>''')

# 6 aftermath 3
pages.append(f'''<section class="page">
{AFH('사례 2. 프롤로그 캠페인: 튜토리얼을 6장 이야기로')}
<div class="body">
<h5>왜 캠페인인가</h5>
<p>10월 27일 회의에서 7단계 튜토리얼을 캠페인으로 바꾸기로 했습니다. <span class="c">세 직업(국왕, 기사, 귀족)과 기능이</span> 많아 한 번에 가르치면 놓치기 쉬워서, 장마다 기능을 하나씩 켜고 정해진 순서로 직업을 바꿔 가며 배우게 했습니다.</p>
<h5>장별 흐름</h5>
<table><tr><th style="width:15%">장</th><th style="width:9%">분</th><th style="width:12%">직업 전환</th><th>새로 가르치는 것</th></tr>
<tr><td>1 함락</td><td>9.2</td><td>1번</td><td>이동, <span class="c">화면 조작</span>, 공격, <span class="c">스킬 Q 사용</span>, 직업 전환</td></tr>
<tr><td>2 피난처</td><td>11.8</td><td>4번</td><td>영지 창, <span class="c">돈, 빵, 노동력 생산 체인</span>, 병영, 송금, 벽과 포탑</td></tr>
<tr><td>3 피난처의 밤</td><td>6.6</td><td>4번</td><td>낮과 밤, 웨이브, 포탑 집중공격, 드래그와 어택땅, 스킬 배우기, <span class="c">스킬 W 사용</span></td></tr>
<tr><td>4 개척</td><td>12.2</td><td>5번</td><td>정찰, 사냥, 점령지, 망루, 마을 승격, 대장간, <span class="c">유닛 무장</span>, <span class="c">스킬 E 사용</span></td></tr>
<tr><td>5 동맹</td><td>10.1</td><td>7번</td><td>외교 창, <span class="c">세력 요청, 정책</span> 카드, 칙령, 지원군 지휘, <span class="c">스킬 R 사용</span></td></tr>
<tr><td>6 탈환</td><td>8.5</td><td>8번</td><td>부대 지정과 호출</td></tr></table>
<div class="gal"><div><img src="{img(I+'p-005.jpg')}">3장 낮과 밤: 본성을 지키는 웨이브</div><div><img src="{img(I+'p-006.jpg')}">3장 스킬 배우기: 스킬트리 계열 선택</div><div><img src="{img(I+'p-007.jpg')}">2장 영지 창: 촌락, 마을, 도시 단계</div></div>
<h5>설계 원칙</h5>
<ul><li><span class="c">기능은 장마다 하나씩</span> 켭니다. 2장 영지, 3장 낮과 밤, 4장 필드, 5장 외교, 6장 부대 순서입니다.</li>
<li>장 안에서는 경험치가 없고, 장 끝에 <span class="c">정해진 경험치를 지급</span>해 다음 장의 스킬을 엽니다. 배운 스킬은 다음 장으로 이어집니다.</li>
<li>안내 문구나 연출 없이 인물 대사로만 이야기를 전합니다. 스토리 작성 규칙을 문서로 따로 만들어 장마다 같은 기준으로 썼습니다.</li>
<li>목표 시간 90분에 억지로 맞추지 않고, 장마다 계산한 시간(합계 58.4분)을 그대로 따랐습니다.</li>
<li>장마다 체크포인트를 2~3곳 두고, 저장 대신 단계별 고정 상태로 다시 시작합니다.</li></ul>
<div class="box"><b>회고</b>장별 세부 명세와 스크립트를 팀원 두 명에게 나눠 맡겼지만, 업무 범위만 전하고 기준을 문서로 주지 않아 수치와 명시가 빠졌습니다. 팀원들과 상황을 공유해 스테이지 구성과 줄거리는 살리고, 빠진 수치와 대사만 제가 다시 작업해 6장을 완성했습니다. 그 뒤로는 작업 지시를 md 파일로 주고받는 방식이 팀 규칙이 됐습니다.</div>
<p class="small">본인 담당 문서 <span class="c">29건</span>은 사이트 Aftermath 페이지에서 볼 수 있습니다.</p>
</div>{foot('Aftermath 3 / 3')}</section>''')

# 7 echo
bars = [('열쇠 든 점프',2.0),('맨몸 점프',3.3),('잔향 딛기',4.5),('잔향 2단 탑',5.7),('잔향 점프대',7.9)]
bh = ''.join(f'<div class="bar"><div style="height:{v/7.9*26:.1f}mm">{v}</div><span>{n}</span></div>' for n,v in bars)
pages.append(f'''<section class="page">
{hdr('PROJECT 03 | 개인 프로젝트','잔향 (Echo)','"10초 전의 내가 지금의 동료가 된다", 시간 루프 퍼즐 플랫포머','Unity 6<br>Windows 빌드 v1.0')}
<div class="body">
<div class="stats"><div class="stat"><b>30</b><span>방 (스테이지 10 × 3)</span></div><div class="stat"><b>10+</b><span>기믹 종류</span></div><div class="stat"><b>1인</b><span>기획 + AI 협업 구현</span></div><div class="stat"><b>1주</b><span>2026.09.11 ~ 09.18</span></div></div>
<table class="info"><tr><td class="h">장르</td><td>2D 퍼즐 플랫포머 (PC)</td><td class="h">사용 툴</td><td>Unity 6, VS Code, Git, Claude</td></tr></table>
<h5>개요</h5>
<p>10초 동안의 움직임이 녹화되고, 되감으면 그 기록이 '잔향'이 되어 그대로 다시 움직인다. 과거의 내가 발판을 밟아 문을 열고, 닿지 않는 절벽은 과거의 나를 딛고 오른다. 목표 감정은 "내 계획이 맞아떨어지는 순간의 쾌감".</p>
<h5>담당 업무</h5>
<ul><li>컨셉 기획서, WBS 작성, 규칙 설계와 30개 방 레벨 디자인, 이동 방법별 수치 밸런싱</li>
<li>Claude로 구현: 루프, 녹화 시스템, 기믹 10여 종, 로비, HUD, 되감기 연출 / 에디터 스크립트로 30개 방 자동 생성</li></ul>
<div class="gal"><div><img src="{img(I+'p-008.jpg')}">발판과 문: 과거의 내가 문을 연다</div><div><img src="{img(I+'p-009.jpg')}"><span class="c">잔향 2단 탑: 잔향 둘을</span> 쌓아 오른다</div><div><img src="{img(I+'p-010.jpg')}">스테이지 10: 열쇠와 장벽</div></div>
<h5>레벨 설계: 방법별 도달 높이</h5>
<div class="bars">{bh}</div>
<p>절벽 높이를 두 값 사이로 정해 "이 방법이 아니면 오를 수 없는" 방을 만들었다. <span class="c">스테이지마다 방 1에서 새 요소를 소개하고, 방 3에서 앞 요소를 조합한다</span>.</p>
<h5>문제, 판단, 해결</h5>
<table><tr><th style="width:32%">문제</th><th style="width:28%">판단</th><th>해결</th></tr>
<tr><td>잔향 위에 서면 함께 떠오르는 버그</td><td>막기보다 퍼즐 재미로 쓸 수 있다</td><td>'잔향 점프대'를 정식 기믹으로 채택, 스테이지 4~5의 중심 규칙으로</td></tr>
<tr><td>후반 스테이지가 같은 풀이의 변주뿐</td><td>새로 배우는 규칙이 필요하다</td><td>'들면 점프가 낮아지는 열쇠'로 과거의 나에게 심부름 맡기는 퍼즐</td></tr>
<tr><td>마지막 방에서 의도보다 쉬운 풀이</td><td>감이 아닌 수치로 막아야 한다</td><td>점프 속도, 중력으로 이동 거리를 계산해 열쇠, 천장, 절벽 높이 조정</td></tr></table>
<div class="gbox"><b>산출물</b>컨셉 기획서, WBS, 프로젝트 페이지</div>
<div class="box"><b>배운 점</b>기획서는 만드는 사람이 그대로 구현할 만큼 구체적이어야 하고, 의도는 수치와 조건으로 고정해야 지켜진다.</div>
</div>{foot('잔향')}</section>''')

# 8 who am i
emo = open(A+'whoami_emotion.svg',encoding='utf-8').read()
loop = open(A+'whoami_loop.svg',encoding='utf-8').read()
pages.append(f'''<section class="page">
{hdr('PROJECT 04 | 팀 프로젝트','WHO AM I?','감정 곡선 레벨 설계')}
<div class="body">
<h5>추리 미스터리 비주얼 노벨, 팀 내 역할 (5인, <span class="c">Ren'Py, 2026.04.20 ~ 26</span>)</h5>
<table><tr><th style="width:24%">역할</th><th style="width:12%">담당</th><th>범위</th></tr>
<tr><td>일정 관리</td><td>팀원</td><td>팀 일정과 작업 보드 관리</td></tr>
<tr><td>시나리오</td><td>팀원</td><td>세계관과 메인 시나리오</td></tr>
<tr><td><b>시스템, 레벨 디자인</b></td><td><b>본인</b></td><td><b>플레이 루프, 로비 구조, 여섯 방의 감정 단계와 배치 순서, 방별 상호작용 조건</b></td></tr>
<tr><td>이미지 리소스</td><td>팀원</td><td>배경, 캐릭터, UI 이미지</td></tr>
<tr><td>스크립트</td><td>팀원</td><td>장면별 스크립트와 분기</td></tr></table>
<div class="fig" style="width:62%;margin:0 auto">{emo}</div>
<table><tr><th style="width:15%">단계</th><th style="width:20%">방</th><th>설계</th><th style="width:11%">게임 화면</th></tr>
<tr><td>1. 호감</td><td><span class="c">'언제', '어디서'의 방</span></td><td>인물 정보 없이 배경만 서술해 분위기에 몰입시키고 NPC에게 호감을 갖게 함</td><td><img src="{img(I+'p-011.jpg')}" style="width:100%"></td></tr>
<tr><td>2. 의심, 불안</td><td><span class="c">'무엇을', '어떻게'의 방</span></td><td>사건의 실마리를 드러내 1단계의 호감과 부딪히게 함</td><td><img src="{img(I+'p-012.jpg')}" style="width:100%"></td></tr>
<tr><td>3. 혼란, 선택</td><td><span class="c">'왜', '누가'의 방</span></td><td>NPC 정체를 공개하는 '누가'를 마지막 방에 두어 엔딩 선택(기획 3종, 일정상 2종 구현)에 직결</td><td><img src="{img(I+'p-013.jpg')}" style="width:100%"></td></tr></table>
<div class="fig" style="width:24%;margin:0 auto">{loop}</div>
<p>조사, 아이템 획득, 해금, 단서 확인 루프. 스토리 전달이 핵심이라 퍼즐 난이도는 낮추고, 탐색하는 동안 추측이 쌓이도록 했다. <span class="c">레벨 설계 슬라이드는 사이트 WHO AM I? 페이지에서 볼 수 있다.</span></p>
<h5>AI 활용 범위 명시</h5>
<table><tr><th style="width:18%">결과물</th><th style="width:44%">본인</th><th>AI (Claude)</th></tr>
<tr><td>메모리 엔더</td><td>기획, 설계, 튜닝 결정, 플레이 테스트</td><td>코드, 사운드 합성, 문구, 문서 초안</td></tr>
<tr><td>잔향</td><td>기획, 레벨 디자인, 수치 밸런싱</td><td>시스템, 기믹 코드</td></tr>
<tr><td>Aftermath</td><td><span class="c">컨셉 원안, 콘텐츠 기획, 방향 결정</span>, 검토, 수정</td><td>문서 초안, 검산, 충돌 확인</td></tr>
<tr><td>자기소개서</td><td>내용, 경험, 최종 문장 결정</td><td>질문, 문장 순서 정리, 글자 수 맞춤, 일부 문장 초안</td></tr></table>
</div>{foot('WHO AM I?')}</section>''')

html = f'<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(pages)}</body></html>'
open('/home/claude/pdfwork/portfolio_generic.html','w',encoding='utf-8').write(html)

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox','--allow-file-access-from-files'])
    pg = b.new_page(); pg.goto('file:///home/claude/pdfwork/portfolio_generic.html'); pg.wait_for_timeout(800)
    over = pg.evaluate('''()=>[...document.querySelectorAll('.page')].map((s,i)=>{const b=s.querySelector('.body');if(!b)return i+1+':-';const l=[...b.children].pop().getBoundingClientRect().bottom-s.getBoundingClientRect().top;return (i+1)+':'+Math.round(l)+'/'+Math.round(s.getBoundingClientRect().height-38)})''')
    print(' '.join(over))
    pg.pdf(path='/home/claude/pdfwork/portfolio.pdf', prefer_css_page_size=True, print_background=True)
    b.close()
print('ok')
import sys
if len(sys.argv)>1:
    h=open('/home/claude/pdfwork/portfolio_generic.html',encoding='utf-8').read()
    h=h.replace('span.c{}','span.c{background:#fff27a;color:#000;box-shadow:0 0 0 1px #fff27a}.cr td{background:#fff9c4}.cov span.c,.hdr span.c{background:#c9a400;color:#fff;box-shadow:none}').replace("('잔향 2단 탑'","")
    open('/home/claude/pdfwork/marked.html','w',encoding='utf-8').write(h)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox','--allow-file-access-from-files'])
        pg=b.new_page();pg.goto('file:///home/claude/pdfwork/marked.html');pg.wait_for_timeout(800)
        pg.pdf(path='/home/claude/pdfwork/marked.pdf',prefer_css_page_size=True,print_background=True)
        b.close()
    print('marked')
