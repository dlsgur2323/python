
public class Human extends Animal{
	long money_power = 1000000000000L;
	
	@Override
	public void getOld() {
		age += 2;
	}
	
	public void earnMoney() {
		money_power++;
	}
	public void earnMoney(int money) {
		money_power += money;
	}
}
