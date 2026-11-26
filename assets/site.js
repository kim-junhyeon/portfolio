// 유튜브 영상 ID만 채우면 사이트 전체에 영상이 들어갑니다.
// 예: https://youtu.be/AbCdEf12345 → 'AbCdEf12345'
const VIDEOS = {
  'memory-ender': '1gkq9mA3te0',
  'echo': '',
};

document.querySelectorAll('.video[data-v]').forEach(el => {
  const id = VIDEOS[el.dataset.v];
  if (!id) { el.remove(); return; } // 영상이 없으면 자리째 숨김
  el.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${id}?rel=0" title="플레이 영상" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
});

// 갤러리 사진 클릭 확대 (Esc, 바깥 클릭, 좌우 화살표)
(() => {
  const imgs = [...document.querySelectorAll('.gallery img')];
  if (!imgs.length) return;
  const box = document.createElement('div');
  box.className = 'lb';
  box.innerHTML = '<button class="lb-x" aria-label="닫기">×</button><button class="lb-p" aria-label="이전">‹</button><img alt=""><button class="lb-n" aria-label="다음">›</button><div class="lb-c"></div>';
  document.body.appendChild(box);
  const big = box.querySelector('img'), cap = box.querySelector('.lb-c');
  let i = 0;
  const show = k => { i = (k + imgs.length) % imgs.length; big.src = imgs[i].src; cap.textContent = `${imgs[i].alt}  (${i + 1} / ${imgs.length})`; };
  const close = () => box.classList.remove('on');
  imgs.forEach((im, k) => im.addEventListener('click', () => { show(k); box.classList.add('on'); }));
  box.addEventListener('click', e => { if (e.target === box || e.target.classList.contains('lb-x')) close(); });
  box.querySelector('.lb-p').addEventListener('click', e => { e.stopPropagation(); show(i - 1); });
  box.querySelector('.lb-n').addEventListener('click', e => { e.stopPropagation(); show(i + 1); });
  document.addEventListener('keydown', e => {
    if (!box.classList.contains('on')) return;
    if (e.key === 'Escape') close(); else if (e.key === 'ArrowLeft') show(i - 1); else if (e.key === 'ArrowRight') show(i + 1);
  });
})();

// PDF는 새 탭에서 열기 (사이트를 떠나지 않게)
document.querySelectorAll('a[href$=".pdf"]').forEach(a => { a.target = '_blank'; a.rel = 'noopener'; });

// 홈 슬라이더: 화살표, 탭, 좌우 키, 밀어서 넘기기
(() => {
  const sl = document.querySelector('.slider');
  if (!sl) return;
  const view = sl.querySelector('.sl-view'), track = sl.querySelector('.sl-track');
  const panels = [...sl.querySelectorAll('.sl-panel')], tabs = [...document.querySelectorAll('.sl-tab')];
  const prev = sl.querySelector('.sl-arrow.sl-prev'), next = sl.querySelector('.sl-arrow.sl-next');
  let i = 0;
  const go = k => {
    i = Math.max(0, Math.min(panels.length - 1, k));
    track.style.transform = `translateX(${-100 * i}%)`;
    view.style.height = panels[i].offsetHeight + 'px';
    tabs.forEach((t, n) => t.classList.toggle('on', n === i));
    prev.disabled = i === 0; next.disabled = i === panels.length - 1;
  };
  prev.addEventListener('click', () => go(i - 1));
  next.addEventListener('click', () => go(i + 1));
  tabs.forEach((t, n) => t.addEventListener('click', () => go(n)));
  sl.tabIndex = -1;
  document.addEventListener('keydown', e => {
    if (document.querySelector('.lb.on')) return;
    const r = sl.getBoundingClientRect();
    if (r.bottom < 0 || r.top > innerHeight) return;
    if (e.key === 'ArrowRight') go(i + 1); else if (e.key === 'ArrowLeft') go(i - 1);
  });
  let x0 = null;
  view.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
  view.addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) go(i + (dx < 0 ? 1 : -1)); x0 = null; });
  addEventListener('resize', () => go(i));
  addEventListener('load', () => go(i));
  if (location.hash === '#analysis') go(1); else go(0);
})();
