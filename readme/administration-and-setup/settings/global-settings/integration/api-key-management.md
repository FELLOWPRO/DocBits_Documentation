---
description: Instrukcje wyświetlania, kopiowania lub ponownego generowania klucza API
---

# Zarządzanie kluczem API

Zarządzanie kluczami API jest ważnym aspektem, jeśli chodzi o bezpieczeństwo integracji oraz dostępu do usług zewnętrznych za pośrednictwem interfejsów API. Oto kilka kroków zarządzania kluczami API oraz najlepszych praktyk dotyczących ich bezpieczeństwa:

**Wyświetlanie i kopiowanie klucza API:**

* Przejdź do ustawień klucza API na swoim koncie DocBits. Tutaj możesz znaleźć klucz API; kliknij „Kopiuj”, aby skopiować klucz.

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-21 um 16.18.04.png" alt=""><figcaption></figcaption></figure>

**Obsługa kluczy API z myślą o bezpieczeństwie:**

* Traktuj klucze API jak poufne dane uwierzytelniające i nigdy nie udostępniaj ich nikomu. Przechowuj klucze API w bezpieczny sposób i stosuj szyfrowanie, jeśli musisz przechowywać je lokalnie. Regularnie aktualizuj klucze API, aby zapewnić bezpieczeństwo i zminimalizować ryzyko nieautoryzowanego dostępu. Unikaj używania kluczy API w publicznych repozytoriach lub niezabezpieczonych środowiskach, ponieważ mogą one zostać przechwycone przez atakujących.

**Ogranicz uprawnienia klucza API:**

* Nadawaj kluczom API wyłącznie uprawnienia wymagane dla konkretnej integracji lub usługi. Unikaj nadmiernych uprawnień, aby zminimalizować ryzyko nadużyć. Regularnie przeglądaj uprawnienia kluczy API i usuwaj zbędne uprawnienia, gdy nie są już potrzebne.

**Rejestrowanie i monitorowanie wywołań API:**

* Wdróż rejestrowanie i monitorowanie wywołań API, aby wykrywać podejrzane działania lub nietypowe wzorce, które mogą wskazywać na potencjalne naruszenia bezpieczeństwa. Reaguj szybko na podejrzane działania i w razie potrzeby unieważnij naruszone klucze API, aby zminimalizować ryzyko dalszych szkód.

Dzięki starannemu zarządzaniu i zabezpieczaniu kluczy API organizacje mogą zapewnić ochronę swoich integracji oraz dostępu do usług zewnętrznych za pośrednictwem interfejsów API i zminimalizować ryzyko nieautoryzowanego dostępu.
