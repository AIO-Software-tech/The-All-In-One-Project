using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace LoginScreen
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (txtUserName.Text=="Ollie" && txtpassword.Text=="123")
            {
                Process.Start("AIO Launcher.exe");
                this.Hide();
            } else if(txtUserName.Text=="Admin" && txtpassword.Text=="abc")
            {
                Process.Start("AIO Launcher.exe");
                this.Hide();
            } else if(txtUserName.Text=="Imre" && txtpassword.Text=="1233")
            {
                Process.Start("AIO Launcher.exe");
                this.Hide();
            } else if(txtUserName.Text=="Guest" && txtpassword.Text=="1234")
            {
                Process.Start("AIO Launcher.exe");
                this.Hide();
            }

            else
            {
                MessageBox.Show("The User name or password you entered is incorrect, try again");
                txtUserName.Clear();
                txtpassword.Clear();
                txtUserName.Focus();
            }
        }

        private void label2_Click(object sender, EventArgs e)
        {
            txtUserName.Clear();
            txtpassword.Clear();
            txtUserName.Focus();
        }

        private void label3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void txtUserName_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
