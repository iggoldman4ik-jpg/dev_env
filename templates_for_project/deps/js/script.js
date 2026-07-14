// Открытие модальных окон
document.addEventListener('DOMContentLoaded', function() {
    const depositBtn = document.getElementById('deposit-btn');
    const withdrawBtn = document.getElementById('withdraw-btn');
    const changeAccountBtn = document.getElementById('change-account-btn');
    
    const depositModal = document.getElementById('deposit-modal');
    const withdrawModal = document.getElementById('withdraw-modal');
    
    const cancelDeposit = document.getElementById('cancel-deposit');
    const confirmDeposit = document.getElementById('confirm-deposit');
    
    const cancelWithdraw = document.getElementById('cancel-withdraw');
    const confirmWithdraw = document.getElementById('confirm-withdraw');
    
    // Открытие модального окна пополнения
    depositBtn.addEventListener('click', function() {
        depositModal.classList.add('active');
    });
    
    // Открытие модального окна снятия
    withdrawBtn.addEventListener('click', function() {
        withdrawModal.classList.add('active');
    });
    
    // Закрытие модальных окон
    cancelDeposit.addEventListener('click', function() {
        depositModal.classList.remove('active');
    });
    
    cancelWithdraw.addEventListener('click', function() {
        withdrawModal.classList.remove('active');
    });
    
    // Закрытие модального окна по клику вне области
    window.addEventListener('click', function(event) {
        if (event.target === depositModal) {
            depositModal.classList.remove('active');
        }
        if (event.target === withdrawModal) {
            withdrawModal.classList.remove('active');
        }
    });
    
    // Подтверждение пополнения
    confirmDeposit.addEventListener('click', function() {
        const amount = document.getElementById('deposit-amount').value;
        if (amount && amount > 0) {
            alert(`Сумма ${amount} ₽ успешно зачислена на ваш счет!`);
            depositModal.classList.remove('active');
            document.getElementById('deposit-amount').value = '';
            
            // Обновление баланса (имитация)
            const balanceElement = document.querySelector('.balance-amount');
            let currentBalance = parseInt(balanceElement.textContent.replace(/\s/g, '').replace('₽', ''));
            currentBalance += parseInt(amount);
            balanceElement.textContent = currentBalance.toLocaleString() + ' ₽';
        } else {
            alert('Пожалуйста, введите корректную сумму!');
        }
    });
    
    // Подтверждение снятия
    confirmWithdraw.addEventListener('click', function() {
        const amount = document.getElementById('withdraw-amount').value;
        if (amount && amount > 0) {
            const balanceElement = document.querySelector('.balance-amount');
            let currentBalance = parseInt(balanceElement.textContent.replace(/\s/g, '').replace('₽', ''));
            
            if (parseInt(amount) <= currentBalance) {
                alert(`Сумма ${amount} ₽ успешно снята с вашего счета!`);
                withdrawModal.classList.remove('active');
                document.getElementById('withdraw-amount').value = '';
                
                // Обновление баланса (имитация)
                currentBalance -= parseInt(amount);
                balanceElement.textContent = currentBalance.toLocaleString() + ' ₽';
            } else {
                alert('Недостаточно средств на счете!');
            }
        } else {
            alert('Пожалуйста, введите корректную сумму!');
        }
    });
    
    // Смена аккаунта
    changeAccountBtn.addEventListener('click', function() {
        if (confirm('Вы уверены, что хотите сменить аккаунт?')) {
            window.location.href = 'http://127.0.0.1:5500/index/index.html';
        }
    });
    
    // Закрытие модального окна при нажатии Escape
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            depositModal.classList.remove('active');
            withdrawModal.classList.remove('active');
        }
    });
});
