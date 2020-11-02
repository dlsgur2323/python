package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame04 frame = new MyFrame04();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setBounds(42, 94, 61, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setColumns(10);
		tf2.setBounds(154, 94, 61, 21);
		contentPane.add(tf2);
		
		tf3 = new JTextField();
		tf3.setEditable(false);
		tf3.setColumns(10);
		tf3.setBounds(42, 151, 97, 21);
		contentPane.add(tf3);
		
		JLabel lbl1 = new JLabel("에서");
		lbl1.setBounds(115, 97, 38, 15);
		contentPane.add(lbl1);
		
		JLabel lbl2 = new JLabel("까지 합은");
		lbl2.setBounds(238, 97, 57, 15);
		contentPane.add(lbl2);
		
		JButton btn = new JButton("실행");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int i = Integer.parseInt(tf1.getText());
				int j = Integer.parseInt(tf2.getText());
				int min = Math.min(i, j);
				int max = Math.max(i, j);
				tf3.setText(Integer.toString((min+max)*(max-min+1)/2));
			}
		});
		btn.setBounds(307, 93, 61, 23);
		contentPane.add(btn);
	}

}
