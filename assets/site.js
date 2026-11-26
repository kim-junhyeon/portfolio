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
