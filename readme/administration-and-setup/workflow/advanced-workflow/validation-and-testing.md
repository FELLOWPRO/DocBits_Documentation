# Doğrulama ve Test Etme

Bir Gelişmiş İş Akışı oluştururken, araç çubuğundaki iki denetim, oluşturucudan çıkmadan onu kontrol etmenize olanak tanır. Bunlar *oluşturma sırasında hızlı kontroller* içindir — kaydedilmiş, tekrarlanabilir testler için [Test Manager](../test-manager.md)'ı kullanın.

## Validate

**Validate** denetimine tıklayın (check-circle simgesi veya <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> tuşlarına basın). Doğrulama, grafiği sorunlar açısından kontrol eder — bağlanmamış düğümler, eksik yapılandırma ve geçersiz bağlantılar — ve bunları işaret eder, böylece iş akışı gerçek belgeler üzerinde çalışmadan önce düzeltebilirsiniz.

## Test

Geçerli akışı bir örneğe karşı çalıştırmak ve canlı belgeleri etkilemeden nasıl davrandığını izlemek için **Test** denetimine tıklayın (play simgesi veya <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> tuşlarına basın). Bu, tuval üzerinde az önce yaptığınız bir değişikliği hızlıca doğrulamanın en hızlı yoludur.

## Hangisini ne zaman kullanmalı

- **Oluşturucuda Validate / Test** (bu sayfa) — akışı tasarlarken anında geri bildirim.
- **[Test Manager](../test-manager.md)** — senaryoyu kaydedin, böylece gelecekteki değişikliklerden sonra regresyonları yakalamak için onu daha sonra (ve diğer tüm senaryolarınızla birlikte) yeniden çalıştırabilirsiniz.

## Sonraki adımlar

- Düğüm türlerini ve bağlantıları [Düğümler](nodes.md) sayfasında inceleyin.
- Tüm araç çubuğu ve tuval denetimlerini [Araç Çubuğu ve Tuval](toolbar-and-canvas.md) sayfasında görün.
